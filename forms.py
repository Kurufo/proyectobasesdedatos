from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField,SelectField, BooleanField, SubmitField, DateField, DateTimeField,SearchField, FieldList
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from schema import PerfilUsuario, obtener_perfil_usuario,comprobar_usuario

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
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d')
    ocupacion = StringField('Ocupación', validators=[DataRequired()])
    nacionalidad = StringField('Nacionalidad', validators=[DataRequired()])
    submit = SubmitField('Register')

#Revisar validación del username, agrega datos bien a la base de datos exceptuando si hay duplicados

    def validate_username(self, username):
        user = comprobar_usuario(username.data)
        
    #    #Tengo que revisar esto pa la validacion del username
        if user:
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
    sexo=SelectField('Sexo',choices=[('macho','macho'),('hembra','hembra')],validators=[DataRequired()])
    estado = SelectField('Vive?',choices=[('vivo','si'),('muerto','no')], validators=[DataRequired()])
    familia = StringField('Familia', validators=[DataRequired()])
    nombre_ubic= StringField('Ubicación', validators=[DataRequired()])
    ubicacion = SelectField('Región',choices=[('Arica-Parinacota','Arica-Parinacota'),
                                                 ('Tarapacá','Tarapacá'),
                                                 ('Antofagasta','Antofagasta'),
                                                 ('Atacama','Atacama'),
                                                 ('Coquimbo','Coquimbo'),
                                                 ('Valparaíso','Valparaíso'),
                                                 ('Metropolitana','Metropolitana'),
                                                 ('O''Higgins','O''Higgins'),
                                                 ('Maule','Maule'),
                                                 ('Ñuble','Ñuble'),
                                                 ('Bío Bío','Bío Bío'),
                                                 ('Araucanía','Araucanía'),
                                                 ('Los Ríos','Los Ríos'),
                                                 ('Los Lagos','Los Lagos'),
                                                 ('Aysén','Aysén'),
                                                 ('Magallanes','Magallanes')],validators=[DataRequired()])
    tipo_ubicacion=SelectField('Tipo de ubicación',choices=[('ciudad','ciudad'),
                                                            ('villa','villa'),
                                                            ('pueblo','pueblo'),
                                                            ('rural','rural'),
                                                            ('costa','costa'),
                                                            ('oasis','oasis')],validators=[DataRequired()])
    fecha_hora = DateTimeField('Fecha y hora (Hora:Minuto-día/mes/año)', format='%H:%M-%d/%m/%Y', validators=[DataRequired()])   
    
    #Comportamiento
    alimentacion = SelectField('Alimentación',choices=[('carnivoro','carnivoro'),
                                                            ('granivoro','granivoro'),
                                                            ('herbivoro','herbivoro'),
                                                            ('omnivoro','omnivoro'),
                                                            ('insectivoro','insectivoro'),
                                                            ('nectarivoro','nectarivoro')], validators=[Optional()])
    noct_diur= SelectField('Cronotipo',choices=[('nocturno','nocturno'),
                                                            ('diurno','diurno'),
                                                            ('diurno - nocturno','diurno - nocturno'),
                                                            ('crepuscular','crepuscular'),
                                                            ('diurno - crepuscular','diurno - crepuscular'),
                                                            ('crepuscular - nocturno','crepuscular - nocturno')], validators=[Optional()])
    nido = BooleanField('Presencia de nido', validators=[Optional()])
    tipo_nido=SelectField('Tipo del nido',choices=[("", "---"),('escarbado','escarbado'),
                                                            ('monticulo','montículo'),
                                                            ('madriguera','madriguera'),
                                                            ('cavidad','cavidad'),
                                                            ('cuenco','cuenco'),
                                                            ('plato','plato'),
                                                            ('plataforma','plataforma'),
                                                            ('colgante','colgante'),
                                                            ('esferico','esférico')], validators=[Optional()])

    migra=BooleanField('Migración', validators=[Optional()])
    obs_ad = TextAreaField('Observaciones respecto al comportamiento', validators=[Optional()])
    
    #Apariencia
    
    tamano=SelectField('Tamaño',choices=[('muy grande','muy grande'),
                                                            ('pequeno','pequeño'),
                                                            ('mediano - pequeno','mediano - pequeño'),
                                                            ('mediano - grande','mediano - grande'),
                                                            ('muy pequeno','muy pequeño'),
                                                            ('grande','grande'),
                                                            ('mediano','mediano')], validators=[Optional()])
    color=SelectField('Color',choices=[('blanco','blanco'),
                                                            ('pardo','pardo'),
                                                            ('tornasol','tornasol'),
                                                            ('anaranjado','anaranjado'),
                                                            ('gris','gris'),
                                                            ('cafe','café'),
                                                            ('ocre','ocre'),
                                                            ('rojo','rojo'),
                                                            ('castano','castaño'),
                                                            ('verde','verde'),
                                                            ('azul','azul'),
                                                            ('amarillo','amarillo'),
                                                            ('negro','negro')], validators=[Optional()])
    
    tipo_de_pata=SelectField('Tipo de patas', choices=[('rapaces','rapaces'),
                                                            ('paserinas','paserinas'),
                                                            ('palmeadas','palmeadas'),
                                                            ('cigodactilas','cigodactilas'),
                                                            ('espoloneadas','espoloneadas'),
                                                            ('pectinadas','pectinadas'),
                                                            ('lagopedo','lagopedo'),
                                                            ('semipalmeadas','semipalmeadas'),
                                                            ('pamprodactilas','pamprodactilas'),
                                                            ('anisodactilas','anisodactilas'),
                                                            ('totipalmeadas','totipalmeadas'),
                                                            ('lobulada','lobulada')],validators=[Optional()])
    tipo_de_pico=SelectField('Tipo de pico',choices=[('generalista','generalista'),
                                                            ('insectivoro','insectívoro'),
                                                            ('granivoro','granívoro'),
                                                            ('nectarivoro','nectarívoro'),
                                                            ('frugivoro','frugívoro'),
                                                            ('carpintero','carpintero'),
                                                            ('pico - bolsa','pico - bolsa'),
                                                            ('limicola','limícola'),
                                                            ('filtrador','filtrador'),
                                                            ('pescador','pescador'),
                                                            ('pescador grueso','pescador grueso'),
                                                            ('pescador ganchudo','pescador ganchudo'),
                                                            ('buceador','buceador'),
                                                            ('carronero','carroñero'),
                                                            ('ave de presa','ave de presa'),
                                                            ('plano','plano'),
                                                            ('plano c/caruncula','plano c/caruncula')], validators=[Optional()])
    tipo_de_ala=SelectField('Tipo de alas',choices=[('de planeo','de planeo'),
                                                            ('elevadoras','elevadoras'),
                                                            ('elipticas','elípticas'),
                                                            ('de alta velocidad','de alta velocidad'),
                                                            ('terrestre poco voladora','terrestre poco voladora'),
                                                            ('terrestre no voladora','terrestre no voladora'),
                                                            ('acuatica no voladora','acuática no voladora')], validators=[Optional()])
    obser_adic=TextAreaField('Observaciones respecto a la apariencia', validators=[Optional()])
    #foto
    
    submit = SubmitField('Register')
    
