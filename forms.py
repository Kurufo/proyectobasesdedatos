from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from schema import PerfilUsuario, obtener_perfil_usuario

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    

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

    #Hay que hacer algo parecido, pero pa filtrar emails
    #def validate_email(self, email):
    #    user = User.query.filter_by(email=email.data).first()
    #    if user is not None:
    #        raise ValidationError('Please use a different email address.')
    
class SightingForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    especie = StringField('Especie', validators=[DataRequired()])
    orden = StringField('Orden', validators=[DataRequired()])
    familia = StringField('Familia', validators=[DataRequired()])
    ubicacion = StringField('Ubicación',validators=[DataRequired()])
    fecha_hora = DateField('Fecha y hora', format='%d/%m/%Y', validators=[Optional()])   
    ocupacion = StringField('Ocupación', validators=[DataRequired()])
    nacionalidad = StringField('Nacionalidad', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = obtener_perfil_usuario(username.data)
        
        #Tengo que revisar esto pa la validacion del username
        if user is not None:
            raise ValidationError('Please use a different username.')