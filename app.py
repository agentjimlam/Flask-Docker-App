from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker. My name is Jimmy! version 1.2.0</h2>'


if __name__ == "__main__":
    app.run(debug=True)