from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '欢迎来到flask页面'
@app.route('/<int:pk>')
def detail(pk):
    return f'欢迎来到flask{pk}'

if __name__ == '__main__':
    app.run(host='192.168.11.8', port='5353', debug=True)