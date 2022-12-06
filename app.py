from flask import Flask
from flask import render_template, flash, redirect,url_for, request
from config import Config #Se llama la def desde un archivo aparte
from forms import LoginForm, RegistrationForm, SightingForm
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from werkzeug.security import generate_password_hash
from flask_login import current_user, login_user,logout_user,LoginManager,login_required
from schema import obtener_id_apar,obtener_id_comp,comprobar_usuario,obtener_perfil_usuario, obtener_ingreso_usuario, ingresar_usuario,ingresar_avistamiento,asignar_avistamiento_usuario,obtener_id_avist,hecho_por, ingresar_comp_obs,ingresar_apar_obs,avistamiento_especie,visto_en,que_hacia,como_lucia,se_encuentra_en,cuando
from werkzeug.urls import url_parse

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'

#En el render_template hay que actualizar las templates correspondientes

@login.user_loader
def load_user(iden):
    return obtener_perfil_usuario(iden)


@app.route('/')
@app.route('/index')
def index():
    user={'username': 'Udwe'}
    posts = [
        {
            'author': {'username': 'Udwe'},
            'body': 'Pantalla inicial'
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
            next_page = url_for('index3')
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


@app.route("/new_sighting", methods=['GET', 'POST'])
@login_required
def new_sighting():
    form = SightingForm()
    if form.validate_on_submit():
        idav=obtener_id_avist() + 1
        ingresar_avistamiento(iden=idav, estado=form.estado.data , nido=form.nido.data, sexo=form.sexo.data, estado_cons='bien conservado')
        hecho_por(username=current_user.username, idav=idav)
        avistamiento_especie(especie=form.especie.data,  avistamiento=idav)
        cuando(fecha=form.fecha_hora.data,avistamiento=idav)
        idap=obtener_id_apar()
        idco=obtener_id_comp()
        ingresar_apar_obs(iden=idap, tamano=form.tamano.data, alas=form.tipo_de_ala.data, pico=form.tipo_de_pico.data, patas=form.tipo_de_pata.data, obs_ad=form.obser_adic.data)
        ingresar_comp_obs(iden=idco, alimentacion=form.alimentacion.data, nidificacion=form.tipo_nido.data, migracion=form.migra.data, cronotipo=form.cronotipo.data, obs_ad=form.obs_ad.data)
        que_hacia(idav,idap)
        como_lucia(avistamiento=idav, id_ap=idap)
        visto_en(ubicacion=form.nombre_ubic.data, tipo_localidad=form.tipo_ubicacion.data, region=form.ubicacion.data, avistamiento=idav)
        
        return redirect(url_for('index3'))
    return render_template('hacer_avist.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if comprobar_usuario(form.username.data):
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