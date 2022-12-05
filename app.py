from flask import Flask
from flask import render_template, flash, redirect,url_for, request
from config import Config #Se llama la def desde un archivo aparte
from forms import LoginForm, RegistrationForm, SightingForm
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from werkzeug.security import generate_password_hash
from flask_login import current_user, login_user,logout_user,LoginManager,login_required
from schema import PerfilUsuario,obtener_perfil_usuario,IngresoUsuario, obtener_ingreso_usuario, ingresar_usuario,ingresar_avistamiento,asignar_avistamiento_usuario
from werkzeug.urls import url_parse

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'

#En el render_template hay que actualizar las templates correspondientes

@login.user_loader
def load_user(id):
    return obtener_perfil_usuario(id)


@app.route('/')
@app.route('/index')
def index():
    user={'username': 'Kurufo'}
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
    return render_template('index3.html', title='Home', user=user,  posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
#pa las contraseñas sería mejor usar un hash, pero por simplicidad quedan así libres
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user=obtener_ingreso_usuario(form.username.data)
        #user = User.query.filter_by(username=form.username.data).first()
        if user is None or (form.password.data!=user.contrasena):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route("/aves")
def aves():
    user = {'username': 'token de aves en general'}
    posts = [
        {
            'author': {'username': 'Kurufo'},
            'body': 'Acá va un ave'
        }
    ]
    return render_template('index3.html', title='Home', user=user, posts=posts)

@app.route("/ave/<ave>")
def ave(ave):
    user = {'username': 'ave'}
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


@app.route("/new_sighting")
#@login_required
def new_sighting():
    form = SightingForm()
    if form.validate_on_submit():
        #Acá falta agregar la id del avistamiento
        idav=0
        ingresar_avistamiento(iden=idav, estado=form.estado.data, nido=form.nido.data, sexo=form.sexo.data, estado_cons=form.estado_cons.data)
        #asignar_avistamiento_usuario(username=current_user.username, avistamiento=avistamiento.id)
        return redirect(url_for('index'))
    return render_template('hacer_avist.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        ingresar_usuario(username=form.username.data, contrasena=form.password.data, nombre=form.nombre.data, apellido=form.apellido.data, fecha_nacimiento=form.fecha_nacimiento.data,ocupacion=form.ocupacion.data,nacionalidad=form.nacionalidad.data , email=form.email.data)
        flash('Usuario registrado con éxito')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/users")
def users():
    user = {'username': 'ra'}
    posts = [
        {
            'author': {'username': 'Atem'},
            'body': 'Sacrifico 3 monstruos para invocacr al dragón alado de Ra!'
        }
    ]
    return render_template('index3.html', title='Home', user=user, posts=posts)

@app.route('/user/<username>')
def user(username):
    user = obtener_perfil_usuario(username)
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)



if __name__ == "__main__":
    app.run()