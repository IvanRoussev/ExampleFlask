from flask import Flask

app = Flask(__name__)


def double_number(number):
    return number * 2


@app.route("/")
def hello():
    return "<h1>HELLO DOCKER :)</h1>"


@app.route("/double/<int:number>")
def double_route(number):
    result = double_number(number)
    return f"The double of {number} is {result}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
