#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    heading = "<h1>Python Operations with Flask Routing and Views</h1>"
    return heading

@app.route('/print/<string:text>')
def show_text(text):
    print(text)
    return f"{text}"

@app.route('/count/<parameter>')
def count(parameter):
    try:
        num = int(parameter)
        return '\n'.join(str(i) for i in range(num)) + '\n'
    except ValueError:
        return "Invalid input", 400

@app.route('/math/<int:first>/<string:operatr>/<int:second>')
def do_math(first, operatr, second):
    if operatr == '+':
        value = first + second
    elif operatr == '-':
        value = first - second
    elif operatr == '*':
        value = first * second
    elif operatr == 'div':
        value = first / second
    elif operatr == '%':
        value = first % second
    else:
        return "Error: Operation not supported."
    
    return str(value)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
