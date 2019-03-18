from bottle import route, run, static_file

# http://127.0.0.1:9999/
@route("/")
def index():
    return static_file("index.html", root=".")

# http://127.0.0.1:9999/echo
@route("/echo")
def echo1():
    return "It isn't fancy, but it's my home page"

# http://127.0.0.1:9999/thing/Balu
@route("/thing/<thing>")
def thing(thing):
    return "Say hello to my little friend: {}".format(thing)

run(host="localhost", port=9999)