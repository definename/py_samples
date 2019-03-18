from bottle import route, run, static_file

@route("/")
def home():
    return "It isn't fancy, but it's my home page"

run(host="localhost", port=9999)