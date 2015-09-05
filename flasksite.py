from flask import Flask, render_template, request, redirect
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    "nick": "password",
    "jess": "mypassword"
    }

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
def hello_world():
    title = "Manatees"
    return render_template('index.html', title=title)

@app.route('/order', methods= ['POST'])
def order():
    return render_template('order.html', title= "Order") 

@app.route('/signup', methods= ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

@app.route('/thank_you', methods= ['POST'])
def thank_you():
    return render_template('thank_you.html')

@app.route('/watch', methods= ['POST'])
@auth.login_required
def watch():
    return render_template('thank_you.html')




if __name__ == '__main__':
    app.run()
    
