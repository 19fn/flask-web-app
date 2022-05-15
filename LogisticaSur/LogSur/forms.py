from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo, Email, DataRequired, ValidationError
from LogSur.models import Usuario

class RegisterForm(FlaskForm):
    nombre = StringField(label="Nombre*", validators=[Length(min=3, max=50, message="El nombre debe tener como minimo 3 letras."), DataRequired(message="Debe ingresar un nombre para poder registrarse.")]) 
    apellido = StringField(label="Apellido")
    email = StringField(label="Correo Electronico*", validators=[Email(message="Correo electronico invalido."), DataRequired()])
    password = PasswordField(label="Contraseña*", validators=[Length(min=8, message="La contraseña debe tener como minimo 8 caracteres."), DataRequired()])
    password_confirmation = PasswordField(label="Repetir Contraseña*", validators=[EqualTo("password", message="Las contraseñas deben ser iguales."), DataRequired()])
    calle = StringField(label="Calle")
    altura = StringField(label="Altura")
    telefono = StringField(label="Teléfono")
    cp = StringField(label="cp")
    acepto_terminos = BooleanField(label="Acepto", validators=[DataRequired(message="Debe aceptar los terminos & condiciones.")])
    submit = SubmitField(label="Crear")

    # Name validation
    def validate_nombre(self,nombre):
        excluded_chars = " *?!'^+%&/()=}][{$#´-_.,;:¿¡¨"
        for char in self.nombre.data:
            if char in excluded_chars:
                raise ValidationError(f"El caracter {char} no esta permitido en el nombre.") 

    # Lastname validation.
    def validate_apellido(self,apellido):
        excluded_chars = " *?!'^+%&/()=}][{$#´-_.,;:¿¡¨"
        for char in self.apellido.data:
            if char in excluded_chars:
                raise ValidationError(f"El caracter {char} no esta permitido en el apellido.")

    # Email validation.
    def validate_email(self, field):
        if Usuario.query.filter_by(correo_electronico=field.data).first():
            raise ValidationError("El correo electronico se encuentra registrado.") 

class LoginForm(FlaskForm):
    email = StringField(label="Correo Electronico*", validators=[DataRequired()])
    password = PasswordField(label="Contraseña*", validators=[DataRequired(message="Debe Ingresar una Contraseña.")])
    remember_me = BooleanField(label="Recordarme")
    submit = SubmitField(label="Ingresar")

    # Email check
    #def validate_email(self,field):
        #if not Usuario.query.filter_by(correo_electronico=field.data).first():
            #raise ValidationError("Correo Electronico o Contraseña Incorrecta")
    
class EnviarForm(FlaskForm):
    nom_remitente = StringField(label="Nombre y Apellido*", validators=[DataRequired(message="Debe ingresar el nombre del remitente")])
    calle_remitente = StringField(label="Calle*", validators=[DataRequired(message="Debe ingresar un domicilio pra el remitente.")])
    altura_remitente = StringField(label="Altura*", validators=[DataRequired(message="Debe ingresar una altura para el domicilio del remitente.")])
    tel_remitente = IntegerField(label="Telefono*", validators=[DataRequired(message="Debe ingresar un telefono para el remitente.")])
    t_servicio = SelectField(label="Servicio", choices=[("Elegir una opción"),("Envío Puerta a Puerta"), ("Envío Sucursal a Sucursal"),("Otro")])
    t_pago = SelectField(label="Pago", choices=[("Elegir una opción"),("Pago en Origen"), ("Pago en Destino"),("Otro")])
    info_remitente = TextAreaField(label="Información Adicional")
    nom_destinatario = StringField(label="Nombre y Apellido*", validators=[DataRequired(message="Debe ingresar el nombre del destinatario.")])
    calle_destinatario = StringField(label="Calle*", validators=[DataRequired(message="Debe ingresar un domicilio para el destinatario")])
    altura_destinatario = StringField(label="Altura*", validators=[DataRequired(message="Debe ingresar una altura para el domicilio del destinatario.")])
    tel_destinatario = IntegerField(label="Telefono*", validators=[DataRequired(message="Debe ingresar un telefono para el destinatario")])
    info_destinatario = TextAreaField(label="Información Adicional")
    recaptcha = RecaptchaField()
    submit = SubmitField(label="Realizar Envio")

class ContactoForm(FlaskForm):
    motivo = SelectField(label="Motivo", choices=[("Seleccioná una opción"),("Quiero conocer el estado de mi envio"),("Tengo una consulta sobre mi envio"),("Otro")])
    nom_ape = StringField(label="Nombre y Apellido", validators=[DataRequired(message="Debe ingresar un nombre para poder contactarlo.")])
    correo = StringField(label="Correo Electronico", validators=[Email(message="Correo Electronico Invalido."),DataRequired(message="Debe ingresar un correo electronico asi podremos contactarte.")])
    msj = TextAreaField(label="Mensaje", validators=[Length(max=1000, message="El mensaje permite como maximo 1000 palabras...")])
    submit = SubmitField(label="Enviar")

    def validate_nom_ape(self,nom_ape):
        excluded_chars = "*?!'^+%&/()=}][{$#´-_.,;:¿¡¨"
        for char in self.nom_ape.data:
            if char in excluded_chars:
                raise ValidationError(f"El caracter {char} no esta permitido en el nombre o apellido.") 
    
    def validate_msj(self,msj):
        excluded_chars = "'¨][`}{_;"
        for char in self.msj.data:
            if char in excluded_chars:
                raise ValidationError(f"El caracter {char} no esta permitido en el mensaje.")


class UpdatePerfil(FlaskForm):
    nombre = StringField(label="Nombre", validators=[DataRequired(message="Debe ingresar un nombre")])
    apellido = StringField(label="Apellido", validators=[DataRequired(message="Debe ingresar un apellido")])
    telefono = StringField(label="Telefono")
    correo = StringField(label="Correo Electronico", validators=[Email(message="El correo electronico ingresado no es valido o ya existe.")])
    password = PasswordField(label="Contraseña*", validators=[Length(min=8, message="La contraseña debe tener como minimo 8 caracteres.")])
    password_confirmation = PasswordField(label="Repetir Contraseña*", validators=[EqualTo("password", message="Las contraseñas deben ser iguales.")])
    calle = StringField(label="Calle")
    altura = IntegerField(label="Altura")
    cp = IntegerField(label="Codigo Postal")
    submit = SubmitField(label="Guardar")

class UpdateEnvios(FlaskForm):
    nombre = StringField(label="Nombre")
    telefono = StringField(label="Telefono")
    calle= StringField(label="Calle")
    altura = IntegerField(label="Altura")
    cp = IntegerField(label="Codigo Postal")
    submit = SubmitField(label="Confirmar")

class PasswdRecoveryForm(FlaskForm):
    correo = StringField(label="Correo Electronico", validators=[Email(message="El correo electronico ingresado no es valido.")])
    submit = SubmitField(label="Enviar")

class EditEnvio(FlaskForm):
    t_servicio = SelectField(label="Servicio", choices=[("Elegir una opción"),("Envío Puerta a Puerta"), ("Envío Sucursal a Sucursal"),("Otro")])
    t_pago = SelectField(label="Pago", choices=[("Elegir una opción"),("Pago en Origen"), ("Pago en Destino"),("Otro")])
    info_remitente = TextAreaField(label="Información Remitente")
    nom_destinatario = StringField(label="Nombre y Apellido Destinatario*", validators=[DataRequired(message="Debe ingresar el nombre del destinatario.")])
    calle_destinatario = StringField(label="Calle Destinatario*", validators=[DataRequired(message="Debe ingresar un domicilio para el destinatario")])
    altura_destinatario = StringField(label="Altura Destinatario*", validators=[DataRequired(message="Debe ingresar una altura para el domicilio del destinatario.")])
    tel_destinatario = IntegerField(label="Telefono Destinatario*", validators=[DataRequired(message="Debe ingresar un telefono para el destinatario")])
    info_destinatario = TextAreaField(label="Información Destinatario")
    submit = SubmitField(label="Guardar")

class Cotizacion(FlaskForm):
    localidad = SelectField(label="Localidad", choices=[("A. Korn"),("Avellaneda"),("Banfield"),("Berazategui"),
                                                        ("Bernal"),("Bosques"),("Boulogne"),("Burzaco"),("CABA"),
                                                        ("Caceros"),("Calzada"),("Campana"),("Cañuelas"),("Ciudadela"),
                                                        ("Del Viso"),("Don Torcuato"),("Escobar"),("Ezeiza"),                                                  
                                                        ("Garin"),("General Rodriguez"),("Hurlingham"),                                                    
                                                        ("Ituzaingo"),("J.C. Paz"),("La Matanza"),("Lanus"),("La Plata"),
                                                        ("Lomas de Zamora"),("Los Polvorines"),("Lujan"),("Marcos Paz"),("Martinez"),
                                                        ("Merlo"),("Monte Grande"),("Moreno"),("Moron"),("Olivos"),("Pacheco"),                                                      
                                                        ("Pilar"),("Quilmes"),("Ranelagh"),("San Isidro"),("San Martin"),("San Miguel"),                                                                                                                
                                                        ("San Vicente"),("Sarandi"),("Solano"),("Temperley"),("Tigre"),("Tortugitas"),
                                                        ("Varela"),("Villa Ballester"),("Zarate")], validators=[InputRequired()])
    kilos = SelectField(label="Peso (kilos)", choices=[("5"),("10"),("20"),("50")], validators=[InputRequired()])
    precio = IntegerField(label="Cotización")
    submit = SubmitField(label="Cotizar")