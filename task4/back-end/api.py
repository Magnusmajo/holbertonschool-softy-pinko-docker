from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello_world():
    return 'Hello Holberton. Welcome to Alexis world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
