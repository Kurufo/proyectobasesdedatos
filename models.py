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











    
    
    
    
    
    
    
    
    
    
###########################################




{% extends "base.html" %}

{% block content %}
    <h1>Register</h1>
    <form action="" method="post">
        {{ form.hidden_tag() }}      
<p>
            {{ form.nombre.label }} <br>
            {{ form.nombre(size=32) }}<br>
            {% for error in form.nombre.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.especie.label }}<br>
            {{ form.especie(size=64) }}<br>
            {% for error in form.especie.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.estado.label }}<br>
            {{ form.estado}}<br>
            {% for error in form.estado.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.familia.label }}<br>
            {{ form.familia(size=32) }}<br>
            {% for error in form.familia.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.sexo.label }}<br>
            {{ form.sexo}}<br>
            {% for error in form.sexo.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
<p>
            {{ form.ubicacion.label }}<br>
            {{ form.ubicacion}}<br>
            {% for error in form.ubicacion.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
</p>
<p>
{{ form.tipo_ubicacion.label }}<br>
            {{ form.tipo_ubicacion}}<br>
            {% for error in form.tipo_ubicacion.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}

        </p>
<p>
            {{ form.fecha_hora.label }}<br>
            {{ form.fecha_hora(size=32) }}<br>
            {% for error in form.fecha_hora.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>

<!--- COMPORTAMIENTO --->

<p>
            {{ form.alimentacion.label }}<br>
            {{ form.alimentacion}}<br>
            {% for error in form.alimentacion.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
<p>
            {{ form.noct_diur.label }}<br>
            {{ form.noct_diur }}<br>
            {% for error in form.noct_diur.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
<p>
            {{ form.nido.label }}<br>
            {{ form.nido }}<br>
            {% for error in form.nido.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>

<p>
            {{ form.migra.label }}<br>
            {{ form.migra }}<br>
            {% for error in form.migra.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>

<p>
            {{ form.obs_ad.label }}<br>
            {{ form.obs_ad(size=500) }}<br>
            {% for error in form.obs_ad.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>

<!--- APARIENCIA --->

<p>
            {{ form.tamano.label }}<br>
            {{ form.tamano }}<br>
            {% for error in form.tamano.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
<p>
            {{ form.color.label }}<br>
            {{ form.color(size=32) }}<br>
            {% for error in form.color.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
<p>
            {{ form.tipo_de_pata.label }}<br>
            {{ form.tipo_de_pata}}<br>
            {% for error in form.tipo_de_pata.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>

<p>
            {{ form.tipo_de_pico.label }}<br>
            {{ form.tipo_de_pico}}<br>
            {% for error in form.tipo_de_pico.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>

<p>
            {{ form.obs_ad.label }}<br>
            {{ form.obs_ad(size=500) }}<br>
            {% for error in form.obs_ad.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
{% endblock %}








