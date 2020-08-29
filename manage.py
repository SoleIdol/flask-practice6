# author:Sole_idol
# filename: manage.py
# datetime:2020/8/19 7:59
"""
session练习
"""
from flask import Flask, render_template, request, redirect
from flask import session

app = Flask(__name__)
# 为session设置一个安全密钥，一个随机字符串
app.secret_key = r'JDSFW#EUIU(Dfydisay987fdsay876&*F87#$E*#&%6t543'


@app.route('/', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        # 创建session
        session['name'] = request.form.get('name')
        session['password'] = request.form.get('password')
        return redirect('/main/')
    else:
        return render_template('login.html')


@app.route('/main/', methods=('POST', 'GET'))
def main():
    # 获取session
    name = session.get('name')
    password = session.get('password')
    return render_template('main.html', name=name, password=password)


@app.route('/logout/')
def logout():
    if session.get('name'):
        session.pop('name')
    if session.get('password'):
        session.pop('password')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
