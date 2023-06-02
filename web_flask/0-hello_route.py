import os
os.environ['FLASK_ENV'] = 'production'

# Rest of your Flask application code

from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', methods=['GET'])
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

