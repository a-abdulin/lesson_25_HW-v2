from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! New day!!!'

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)

