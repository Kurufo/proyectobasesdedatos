from app import db,login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))











#### Base html
       <div>
<hr>
        <a href="{{ url_for('index') }}" style="font-family:Caveat;font-size:300%;" margin=50px>Home</a>
       {% if current_user.is_anonymous %}
        <a href="{{ url_for('login') }}" style="font-family:Caveat;font-size:300%;" margin=50px>Login</a>
        {% else %}
        <a href="{{ url_for('logout') }}" style="font-family:Caveat;font-size:300%;" margin=50px>Logout</a>
        <a href="{{ url_for('user', username=current_user.username) }}" style="font-family:Caveat;font-size:300%;" margin=50px>Perfil</a>
        {% endif %}
        <a href="{{ url_for('ave') }}" style="font-family:Caveat;font-size:300%;" margin=50px>Aves</a>
        <a href="{{ url_for('user') }}" style="font-family:Caveat;font-size:300%;" margin=50px>Usuarios</a>
<hr>
    </div>
    
### forms .py

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%d/%m/%Y', validators=[Optional()])
    ocupacion = StringField('Ocupación', validators=[DataRequired()])
    nacionalidad = StringField('Nacionalidad', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = obtener_perfil_usuario(username.data)
        
        #Tengo que revisar esto pa la validacion del username
        if user is not None:
            raise ValidationError('Please use a different username.')