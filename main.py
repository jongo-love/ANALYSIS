#creating a flask application.
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/insight')
def insight():
    return render_template('insight.html')

@app.route('/logout')
def logout():
    # Logout logic goes here
    return 'Logout Page'

@app.route('/signin')
def signin():
    # Sign in logic goes here
    return 'Sign In Page'

@app.route('/signup')
def signup():
    # Sign up logic goes here
    return 'Sign Up Page'

if __name__ == '__main__':
    app.run(debug=True)