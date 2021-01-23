from flask import request,render_template,session,url_for,redirect,flash,Blueprint


users = [
    {
        'email': '123456@qq.com',
        'password': '123456'
    }
]
userbp = Blueprint('user',__name__)
@userbp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html', **locals())
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        for u in users:
            if u['email'] == email and u['password'] == password:
                session['user'] = email
                return redirect(url_for('main.index'))
        flash('邮箱或密码错误')
        return redirect(url_for('user.login'))


@userbp.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('main.index'))


@userbp.route('/regist', methods=['GET', 'POST'])
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
                return redirect(url_for('user.regist'))
        if password != password2:
            flash('密码不一致')
            return redirect(url_for('user.regist'))
        users.append({
            'email': email,
            'password': password
        })
        return redirect(url_for('user.login'))