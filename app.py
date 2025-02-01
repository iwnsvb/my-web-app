from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Ubuntu! 这是一个简单的网页应用。"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
