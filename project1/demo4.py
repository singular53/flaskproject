from flask import Flask, render_template, request, url_for, redirect, session,flash

app = Flask(__name__)
app.secret_key = 'asdasdlaksjdlajdklasdlklasd'
book = {
    'title': '天下无双',
    'name': '失落叶',
    'article': [
        {
            'id': 1,
            'chapter': '第一章 -  惊变',
            'content': '一阵尖利的刹车声在公路上响起，鲜血横流，一个女人躺在了马路上，身下满是鲜血，出车祸了！'
        },
        {
            'id': 2,
            'chapter': '第二章 -  死灵剑士',
            'content': '吃掉了半斤牛肉，喝掉几杯酒，身体却并不是很暖和，很是奇怪。'
        },
        {
            'id': 3,
            'chapter': '第三章 -  超级大耳兔',
            'content': '这是我的第一反应，嗯，该冲上去把它做了，说不定能把手里的法杖爆出来，这法杖看起来不错的样子。'
        }
    ]
}
users = [
    {
        'email': '123456@qq.com',
        'password': '123456'
    }
]


@app.route('/')
def index():
    articles = book['article']
    return render_template('index.html', **locals())


@app.route('/<int:pk>')
def detail(pk):
    article = None
    for a in book['article']:
        if a['id'] == pk:
            article = a
    return render_template('detail.html', **locals())


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html', **locals())
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        for u in users:
            if u['email'] == email and u['password'] == password:
                session['user'] = email
                return redirect(url_for('index'))
        flash('邮箱或密码错误')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))


@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html', **locals())
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        global users
        for u in users:
            if u['email'] == email:
                flash('邮箱已注册')
            elif password != password2:
                flash('密码不一致')
                return redirect(url_for('regist'))
        users.append({
            'email': email,
            'password': password
        })
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
