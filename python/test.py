from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "asdf"

if __name__ == '__main__':
    app.run(debug=1,host="localhost",port=3000)