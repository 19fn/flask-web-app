from LogSur import db, bcrypt, login_man
from flask_login import UserMixin

@login_man.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Tables
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(length=50), nullable=False)
    apellido = db.Column(db.String(length=50))
    correo_electronico = db.Column(db.String(length=50), nullable=False, unique=True)
    contraseña_hash = db.Column(db.String(length=60), nullable=False)
    telefono = db.Column(db.String(length=40))
    calle = db.Column(db.String(length=60))
    altura = db.Column(db.Integer())
    cp = db.Column(db.Integer())

    @property
    def contraseña(self):
        return self.contraseña
    
    @contraseña.setter
    def contraseña(self,password):
        self.contraseña_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    
    def check_password(self,password):
        return bcrypt.check_password_hash(self.contraseña_hash,password)
    

class Envio(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre_apellido_rem = db.Column(db.String(length=50), nullable=False)
    calle_rem = db.Column(db.String(length=80), nullable=False)
    altura_rem = db.Column(db.String(length=20))
    telefono_rem = db.Column(db.String(length=50), nullable=False)
    servicio = db.Column(db.String(length=50))
    pago = db.Column(db.String(length=50))
    info_rem = db.Column(db.String(length=1024))
    nombre_apellido_des = db.Column(db.String(length=50), nullable=False)
    calle_des = db.Column(db.String(length=80), nullable=False)
    altura_des = db.Column(db.String(length=20))
    telefono_des = db.Column(db.String(length=50))
    info_des = db.Column(db.String(length=1024))
    usuario_id = db.Column(db.Integer(), db.ForeignKey("usuario.id"))

class EnvioCancelado(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre_apellido_rem = db.Column(db.String(length=50), nullable=False)
    calle_rem = db.Column(db.String(length=80), nullable=False)
    altura_rem = db.Column(db.String(length=20))
    telefono_rem = db.Column(db.String(length=50), nullable=False)
    servicio = db.Column(db.String(length=50))
    pago = db.Column(db.String(length=50))
    info_rem = db.Column(db.String(length=1024))
    nombre_apellido_des = db.Column(db.String(length=50), nullable=False)
    calle_des = db.Column(db.String(length=80), nullable=False)
    altura_des = db.Column(db.String(length=20))
    telefono_des = db.Column(db.String(length=50))
    info_des = db.Column(db.String(length=1024))
    usuario_id = db.Column(db.Integer())
    envio_id = db.Column(db.Integer())

class Contacto(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    motivo = db.Column(db.String(50))
    nombre_apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    mensaje = db.Column(db.String(1024))