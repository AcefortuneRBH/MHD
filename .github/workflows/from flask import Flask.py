from flask import Flask
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config.from_pyfile('.env')

# Initialize cryptography
secret_key = app.config['SECRET_KEY']
cipher_suite = Fernet(secret_key)

# Example route
@app.route('/')
def index():
    return "Blockchain node is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
