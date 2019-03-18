# http://127.0.0.1:9999
# http://127.0.0.1:9999/echo/Godzilla

from flask import Flask
app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/echo/<thing>")
def echo(thing):
    return "Say hello to my little friend: {}".format(thing)

app.run(port=9999, debug=True)