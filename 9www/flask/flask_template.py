from flask import Flask, render_template, request
app = Flask(__name__)

# http://127.0.0.1:9999/args/Tiger
@app.route("/args/<thing>")
def args(thing):
    print("args")
    return render_template("flask2.html", thing=thing)

# http://127.0.0.1:9999/echo_args1/Tiger/Zoo
@app.route("/echo_args1/<thing>/<place>")
def echo_args1(thing, place):
    print("echo_args1")
    return render_template("flask3.html", thing=thing, place=place)

# http://127.0.0.1:9999/echo_args3?thing=Tiger&place=Zoo
@app.route("/echo_args3/")
def echo_args3():
    print("echo_args3")
    thing = request.args.get("thing")
    place = request.args.get("place")
    return render_template("flask3.html", thing=thing, place=place)

# http://127.0.0.1:9999/echo_args4?thing=Tiger&place=Zoo
@app.route("/echo_args4/")
def echo_args4():
    print("echo_args4")
    kwargs = {}
    kwargs["thing"] = request.args.get("thing")
    kwargs["place"] = request.args.get("place")
    return render_template("flask3.html", **kwargs)

app.run(port=9999, debug=True)
