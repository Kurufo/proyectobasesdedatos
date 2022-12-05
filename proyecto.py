from flask import Flask
from flask import render_template, flash, redirect,url_for
from config import Config #Se llama la def desde un archivo aparte
from forms import LoginForm


app = Flask(__name__)
app.config.from_object(Config)


#from app import routes
#from app import app

@app.route('/')
@app.route('/index')
#def home():
 #   return "Hello, World!"
#def index():
 #   return "Hello, World!"
#def index():
#    user={'username':'Kurufo'}
#    return render_template('index.html', title='Home', user=user)
def index():
    user = {'username': 'Kurufo'}
    posts = [
        {
            'author': {'username': 'Aracena'},
            'body': 'Te falta agregar más páginas a tu tesis Víctor'
        },
        {
            'author': {'username': 'Víctor'},
            'body': 'No joda profe'
        }
    ]
    return render_template('index3.html', title='Home', user=user, posts=posts)

#set FLASK_APP=proyecto.py

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == "__main__":
    app.run()