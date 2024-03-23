from flask import Flask, render_template, request, redirect, url_for, sessions
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'XXXXXXXXXX'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists in the database
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            sessions['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
def logout():
    sessions.pop('username', None)
    return redirect(url_for('index'))

@app.route('/users')
def display_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/')
def index():
    if 'username' in sessions:
        return render_template('index.html', username=sessions['username'])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    # Create all tables in the database
    app.run(debug=True)