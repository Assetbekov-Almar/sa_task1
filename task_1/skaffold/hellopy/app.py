import os
import json

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return 'Task 1: hello from ' + os.environ['HOSTNAME'] + ' !'

@app.route("/health")
def health():
	return '{"status": "ok"}'

@app.route("/version")
def version():
	return '{"version": "1.1"}'


if __name__ == "__main__":
	app.run(host='0.0.0.0',port='80')