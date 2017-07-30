from flask  import Flask, render_template, request, redirect, url_for, session
import sqlite3 
app = Flask(__name__)
conn = sqlite3.connect('blog.db')


conn.execute('''CREATE TABLE IF NOT EXISTS Blogs
        (ID      INTEGER PRIMARY KEY,
        NAME            TEXT    NOT NULL,
        TOPIC            TEXT   NOT NULL,
        DESCRIPTION      TEXT   NOT NULL);''')

conn.execute('''CREATE TABLE IF NOT EXISTS User
        (USERNAME         TEXT  NOT NULL,
        PASSWORD         TEXT  NOT NULL);''')
        
conn.close()

@app.route('/')
def home():
    return render_template('bloghome1.html')

@app.route('/sign', methods=['POST','GET'])
def sign():
    if request.method == 'POST':
        conn=sqlite3.connect("blog.db")
        username = request.form['usrnme']
        password = request.form['paswrd']
        confirmpassword = request.form['cnfpswrd']
        if not username or not password or not confirmpassword:
            error = 'all fields required'
            return render_template('signin.html', error = error)
        if password == confirmpassword:
            sql = "SELECT * from User WHERE USERNAME = '%s'" % (username)
            user = conn.execute(sql)
            print user
            userlis = list(user)
            if len(userlis) == 0:
                sql = "INSERT INTO User (USERNAME,PASSWORD) VALUES ('%s','%s')" %(username,password)    
                conn.execute(sql)
                conn.commit()
                conn.close()    
                return redirect('/login')
            else:
                error = 'user already exist'
                return render_template('signin.html', error = error)
        else:
            error = 'password mismatch'
            return render_template('signin.html', error = error)    
    return render_template('signin.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn=sqlite3.connect("blog.db")
        username = request.form['username']
        password = request.form['password']
        print username, password
        if username  == '' or password == '':
            error = 'invalid username or password'
            return render_template('login.html', error = error)
        else:
            sql = "SELECT * from 'user' WHERE USERNAME='"+username+"'"
            print sql
            user = conn.execute(sql)
            user=user.fetchall()
            print user
            if not user:
                error = 'user not exist'

            elif user[0][1] != password:
                error =  'inavalid password'
                print username , password 
            else:
                session['username'] = username
                return redirect('/enternew')
        print error,'error'
        return render_template('login.html', error = error)
    else:
        return render_template('login.html')

            
        

@app.route('/enternew')
def new_member():
    return render_template('member.html')


@app.route('/memb',methods = ['POST', 'GET'])
def memb():
    if request.method == 'POST':
        nme = request.form['nme']
        top = request.form['top']
        desc = request.form['desc']
        print nme
        conn=sqlite3.connect("blog.db") 
        cur = conn.cursor()

        cur.execute("INSERT INTO blogs (name,topic,description) VALUES ('%s','%s','%s')" %(nme,top,desc))
        conn.commit()
        conn.close()
        return render_template('success.html')
    

@app.route('/show')
def show_details():
    conn=sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute("SELECT * from Blogs")
    rows = cur.fetchall()
    print 'rows',rows
    # for row in rows: 
        # print row
    conn.commit()
    conn.close()
    return render_template('show.html',rows = rows)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'       

if __name__== '__main__':
   app.run(debug = True)


   