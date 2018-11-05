import socket
from flask import Flask, request
import usermanage

app = Flask(__name__)


@app.route('/')
def main():
    return 'this is index'


@app.route('/login')
def login():
    pass


@app.route('/register')
def login():
    pass


@app.route('/login')
def login():
    pass


if __name__ == '__main__':
    SERVER_FOLDER = '/server'
    IP = str(socket.gethostbyname(socket.gethostname()))
    app.run(host=IP, debug=True, port=12345)
