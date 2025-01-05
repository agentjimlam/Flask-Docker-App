from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker. My name is Jimmy! Re-tagged image to be called container-assignment.</h2>'


if __name__ == "__main__":
    app.run(debug=True)