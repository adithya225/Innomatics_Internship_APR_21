from flask import Flask, render_template, session, redirect, url_for, escape, request
import random
import string

N = 5

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_uppercase +
                                        string.digits, k=N))
from datetime import datetime

dateNow = datetime.now().strftime('%d - %B - %Y')
task = []


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return (
                    'Logged in as ' + username + '<br>' + "<b><a href = '/logout'> click here to log out from your account </a></b><br>" + "<b><a href = '/bin'>  Save Your Notes </a></b>")
    return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' not in session:
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''

    <form action = "" method = "post">
        <p><input type ='text' name ='username'/></p>
        <p><input type ='submit' value ='Login'/></p>
    </form>	
    '''
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/bin', methods=["GET", "POST"])
def add():
    if 'username' in session:
        print("session call")
        if request.method == 'POST':
            # print("Function calle")
            p = request.form.get("task")
            q = str(session['username'])
            task.extend([q, p])
            print(task)


    else:
        print("not call")
        return redirect(url_for('index'))
    return render_template('home.html', notes=task, k=len(task), p=session['username'], tt=dateNow)


if __name__ == '__main__':
    app.run(debug=True)