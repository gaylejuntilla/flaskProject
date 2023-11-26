from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


# def convert_celsius_to_fahrenheit(celsius):
#     """Convert celsius to fahrenheit"""
#     return celsius * 9.0 / 5 + 32


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=""):
    return f"Input value: {celsius}, result: {float(celsius) * 9.0 / 5 + 32}"


if __name__ == '__main__':
    app.run()
