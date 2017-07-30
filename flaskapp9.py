from flask import Flask, redirect, url_for, render_template, request,session
app = Flask(__name__)

app.secret_key = 'any random string'


@app.route('/')
def index():
    return render_template('login1.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form ['username'] == 'admin' and request.form ['password'] == 'admin':
            user=request.form['username']
            session['username']=user
            return redirect('/success')
        else:
            return render_template('login1.html')
            


@app.route('/success')
def success():
    user=session['username']
    return render_template('success.html',name=user)


if __name__ == '__main__':
    app.run(debug = True)