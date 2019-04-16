import AWSIoTPythonSDK.MQTTLib as mqtt
import time
import logging
import json
import argparse

# Read in command-line parameters
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="Your AWS IoT custom endpoint")
parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
parser.add_argument("-c", "--cert", action="store", dest="certificatePath", help="Certificate file path")
parser.add_argument("-k", "--key", action="store", dest="privateKeyPath", help="Private key file path")
parser.add_argument("-p", "--port", action="store", dest="port", type=int, help="Port number override")
parser.add_argument("-w", "--websocket", action="store_true", dest="useWebsocket", default=False, help="Use MQTT over WebSocket")
parser.add_argument("-n", "--thingName", action="store", dest="thingName", default="Bot", help="Targeted thing name")
parser.add_argument("-id", "--clientId", action="store", dest="clientId", default="5c884ae4-551f-11e9-8647-d663bd873d93", help="Targeted client id")

args = parser.parse_args()
host = args.host
rootCAPath = args.rootCAPath
certificatePath = args.certificatePath
privateKeyPath = args.privateKeyPath
port = args.port
useWebsocket = args.useWebsocket
thingName = args.thingName
clientId = args.clientId

if args.useWebsocket and args.certificatePath and args.privateKeyPath:
    parser.error("X.509 cert authentication and WebSocket are mutual exclusive. Please pick one.")
    exit(2)

if not args.useWebsocket and (not args.certificatePath or not args.privateKeyPath):
    parser.error("Missing credentials for authentication.")
    exit(2)

# Port defaults
if args.useWebsocket and not args.port:  # When no port override for WebSocket, default to 443
    port = 443
if not args.useWebsocket and not args.port:  # When no port override for non-WebSocket, default to 8883
    port = 8883

# Configure logging
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("jd")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTShadowClient
shadowClient = None
if useWebsocket:
    shadowClient = mqtt.AWSIoTMQTTShadowClient(clientId, useWebsocket=True)
    shadowClient.configureEndpoint(host, port)
    shadowClient.configureCredentials(rootCAPath)
else:
    shadowClient = mqtt.AWSIoTMQTTShadowClient(clientId)
    shadowClient.configureEndpoint(host, port)
    shadowClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTShadowClient configuration
shadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
shadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
shadowClient.configureMQTTOperationTimeout(5)  # 5 sec

mqttClient = shadowClient.getMQTTConnection()
mqttClient.configureOfflinePublishQueueing(-1, mqtt.DROP_OLDEST)

shadowClient.onOnline = lambda: logger.debug("MQTT client online event signaled")
shadowClient.onOffline = lambda: logger.debug("MQTT client offline event signaled")

# Connect to AWS IoT
logger.debug("MQTT client connected: {}".format(shadowClient.connect()))

# Create a deviceShadow with persistent subscription
shadowHandler = shadowClient.createShadowHandlerWithName(thingName, True)

def ShadowUpdateCallback(payload, responseStatus, token):
    try:
        if responseStatus == "timeout":
            logger.warning("Update request: {} time out".format(token))
        elif responseStatus == "accepted":
            logger.debug("Update request: {} accepted: {}".format(token, json.loads(payload)["state"]))
        elif responseStatus == "rejected":
            logger.warning("Update request: {} rejected".format(token))
        else:
            logger.debug("Unknown update response status: {}".format(responseStatus))
    except Exception as e:
        logger.error("Shadow update callback error: {}".format(e))

def ShadowDeltaCallback(payload, responseStatus, token):
    try:
        payloadDict = json.loads(payload)
        logger.debug("Delta message received: {}".format(payloadDict))

        reportedDict = { "state" : { "reported": payloadDict["state"], "desired": None } }
        reportedJson = json.dumps(reportedDict)
        logger.debug("Delta request to update the reported state: {}".format(
            shadowHandler.shadowUpdate(reportedJson, ShadowUpdateCallback, 5)))
    except Exception as e:
        logger.error("Shadow delta callback error: {}".format(e))

shadowHandler.shadowRegisterDeltaCallback(ShadowDeltaCallback)

desc = """Usage:
    'on'  - turn on device led;
    'off' - turn off device led;
    'x'   - exit;
    '?'   - get this help."""

def main():

    logger.debug("\n {}".format(desc))

    while True:
        try:
            val = input()
            if val == "on" or val == "off":
                payloadDict = { "state": { "reported": { "led": val }, "desired": None } }
                logger.debug("Update request: {} has been sent".format(
                    shadowHandler.shadowUpdate(json.dumps(payloadDict), ShadowUpdateCallback, 5)))
            elif val == "x":
                break
            elif val == "?":
                logger.debug("\n {}".format(desc))
            else:
                logger.warning("Invalid value: {} was given".format(val))
        except Exception as e:
            logger.error("Error occurred: {}".format(e))

if __name__ == "__main__":
    main()