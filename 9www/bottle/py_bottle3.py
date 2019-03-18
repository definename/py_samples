# Use this url: http://127.0.0.1:9999/echo/Oleh to test this sample

from bottle import route, run, static_file

@route("/")
def main():
    return static_file("index.html", root=".")

@route("/echo/<thing>")
def echo(thing):
    return "Say hello to my little friend: {}".format(thing)

run(host="localhost", port=9999)