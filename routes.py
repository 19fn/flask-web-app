from LogSur import app, db
from LogSur.models import Usuario, Envio, Contacto, EnvioCancelado
from flask import render_template, url_for, redirect, flash, session, request
from LogSur.forms import RegisterForm, LoginForm, EnviarForm, ContactoForm, UpdateEnvios, UpdatePerfil, PasswdRecoveryForm
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.datastructures import MultiDict

# Routes
@app.route("/")
@app.route("/inicio.html")
def home_page():
    return render_template("/inicio.html")

@app.route("/mapa.html")
def map_page():
    return render_template("/mapa.html")

@app.route("/login.html", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user_to_login = Usuario.query.filter_by(correo_electronico=form.email.data).first()
        if user_to_login and user_to_login.check_password(password=form.password.data):
            login_user(user_to_login)
            flash(f"¡Hola {user_to_login.nombre}, me alegra verte!", category="success")
            session.permanent = True
            return redirect(url_for("profile_page"))
        else:
            flash("Correo Electronico o Contraseña Incorrecta.", category="danger")
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"{err_msg}", category="danger")
    return render_template("/login.html", form=form)

@app.route("/logout.html")
@login_required
def logout_page():
    logout_user()
    flash("¡ Has salido correctamente !",category="info")
    return redirect(url_for("home_page"))

@app.route("/profile.html", methods=["GET", "POST"])
@login_required
def profile_page():
    perf = UpdatePerfil()
    if request.method == 'GET':
        nombre = "Fede"
        apellido = "Cabrera"    
        perf = UpdatePerfil(formdata=MultiDict({'nombre': f'{nombre}', 'apellido' : f'{apellido}'}))
    if request.method == "POST":
        perfil_id = request.form.get("perf")
        perfil_obj = Usuario.query.filter_by(id=perfil_id).first()
        perfil_obj.nombre=perf.nombre.data
        perfil_obj.apellido=perf.apellido.data
        perfil_obj.telefono=perf.telefono.data
        perfil_obj.calle=perf.calle.data
        perfil_obj.altura=perf.altura.data
        perfil_obj.cp=perf.cp.data
        db.session.commit()
        flash("Datos actualizados correctamente.", category="success")
        
    perfil = Usuario.query.filter_by(id=current_user.id)
    return render_template("/profile.html", perfil=perfil, perf=perf)

@app.route("/register.html", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        crear_usuario = Usuario( nombre=form.nombre.data,
                                 apellido=form.apellido.data,
                                 correo_electronico=form.email.data,
                                 contraseña=form.password.data)
        db.session.add(crear_usuario)
        db.session.commit()
        login_user(crear_usuario)
        flash(f"Se ha creado el usuario correctamente, ¡ Bienvenido/a {crear_usuario.nombre} !", category="success")
        session.permanent = True
        return redirect(url_for("profile_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"{err_msg}", category="danger")
    return render_template("/register.html", form=form)

@app.route("/contacto.html", methods=["GET","POST"])
def contact_page():
    form = ContactoForm()
    if form.validate_on_submit():
        enviar_mensaje = Contacto(  motivo=form.motivo.data,
                                    nombre_apellido=form.nom_ape.data,
                                    email=form.correo.data,
                                    mensaje=form.msj.data )
        db.session.add(enviar_mensaje)
        db.session.commit()
        flash(f"¡{enviar_mensaje.nombre_apellido} gracias por contactarse! En breve nos comunicaremos con usted.", category="success")
        return redirect(url_for("contact_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"{err_msg}", category="danger")
    return render_template("/contacto.html", form=form)

@app.route("/enviar.html", methods=["GET", "POST"])
@login_required
def enviar_page():
    form = EnviarForm()
    if form.validate_on_submit():
        realizar_envio = Envio( nombre_apellido_rem=form.nom_remitente.data,
                                calle_rem=form.calle_remitente.data,
                                altura_rem=form.altura_remitente.data,
                                telefono_rem=form.tel_remitente.data,
                                servicio=form.t_servicio.data,
                                pago=form.t_pago.data,
                                info_rem=form.info_remitente.data,
                                nombre_apellido_des=form.nom_destinatario.data,
                                calle_des=form.calle_destinatario.data,
                                altura_des=form.altura_destinatario.data,
                                telefono_des=form.tel_destinatario.data,
                                info_des=form.info_destinatario.data,
                                usuario_id=current_user.id)
        db.session.add(realizar_envio)
        db.session.commit()
        flash(f"Se realizó exitosamente el envio con número de identificación: {realizar_envio.id}", category="success")
        return redirect(url_for("enviar_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"{err_msg}", category="danger")
    return render_template("/enviar.html", form=form)

@app.route("/envios.html", methods=["GET","POST"])
@login_required
def mis_envios_page():
    c_envio = UpdateEnvios()
    cancelar_envio = UpdateEnvios()

    if request.method == "POST":
        envio_cancelado = request.form.get("cancelar_envio")
        envio_cancelado_obj = Envio.query.filter_by(id=envio_cancelado).first()
        if envio_cancelado_obj:
            envio_cancel = EnvioCancelado(  nombre_apellido_rem=envio_cancelado_obj.nombre_apellido_rem,
                                            calle_rem=envio_cancelado_obj.calle_rem,
                                            altura_rem=envio_cancelado_obj.altura_rem,
                                            telefono_rem=envio_cancelado_obj.telefono_rem,
                                            servicio=envio_cancelado_obj.servicio,
                                            pago=envio_cancelado_obj.pago,
                                            info_rem=envio_cancelado_obj.info_rem,
                                            nombre_apellido_des=envio_cancelado_obj.nombre_apellido_des,
                                            calle_des=envio_cancelado_obj.calle_des,
                                            altura_des=envio_cancelado_obj.altura_des,
                                            telefono_des=envio_cancelado_obj.telefono_des,
                                            info_des=envio_cancelado_obj.info_des,
                                            usuario_id=current_user.id,
                                            envio_id=envio_cancelado_obj.id)
            db.session.add(envio_cancel)
            db.session.delete(envio_cancelado_obj)
            db.session.commit()
            flash(f"Envío '{envio_cancelado_obj.id}' cancelado exitosamente.", category="success")

        borrar_envio = request.form.get("c_envio")
        borrar_envio_obj = EnvioCancelado.query.filter_by(id=borrar_envio).first()
        if borrar_envio_obj:
            db.session.delete(borrar_envio_obj)
            db.session.commit()
            flash(f"Envío '{borrar_envio_obj.envio_id}' borrado exitosamente.", category="success")

        return redirect(url_for("mis_envios_page"))

    if request.method == "GET":
        envios = Envio.query.filter_by(usuario_id=current_user.id)
        can_envio = EnvioCancelado.query.filter_by(usuario_id=current_user.id)
        return render_template("/envios.html", envios=envios, cancelar_envio=cancelar_envio, c_envio=c_envio, can_envio=can_envio)
        
    if cancelar_envio.errors != {}:
        for err_msg in cancelar_envio.errors.values():
            flash(f"{err_msg}", category="danger")
    if c_envio.errors != {}:
        for err_msg in c_envio.errors.values():
            flash(f"{err_msg}", category="danger")

@app.route("/password_recovery.html", methods=["GET","POST"])
def passwd_recovery():
    form = PasswdRecoveryForm()
    if form.validate_on_submit():
        correo =  Usuario.query.filter_by(correo_electronico=form.correo.data).first()
        if correo:
            if correo.correo_electronico == form.correo.data:
                flash("Se envió un correo con los pasos a seguir para recuperar su contraseña.", category="info")
        else:
            flash("No se encontró una cuenta vinculada al correo electronico ingresado.", category="danger")

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"{err_msg}", category="danger")

    return render_template("/password_recovery.html", form=form)
