from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'wjh'
    age = '18'
    return render_template('index.html',**locals())


if __name__ == '__main__':
    app.run(debug=True)