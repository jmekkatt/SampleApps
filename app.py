from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(5)
    return 'Hey, we have Flask in a Docker container -- By Jaya!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
