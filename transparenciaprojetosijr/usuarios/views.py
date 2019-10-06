from flask import Blueprint, render_template, redirect, flash, request, abort, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from transparenciaprojetosijr import login_manager, db
from transparenciaprojetosijr.usuarios.forms import LoginForm, AdicionarUserForm, EditarUserForm, LogoutForm
from flask_bcrypt import Bcrypt
from transparenciaprojetosijr.usuarios.models import Usuario

usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@usuarios.route("/adicionar", methods=['POST', 'GET'])
def adicionar():
    login=LoginForm()
    adicionar=AdicionarUserForm()
    logout = LogoutForm()

    bcrypt= Bcrypt()
    busca  = Usuario.query.filter_by(email=adicionar.email.data).first()
	
    if not busca:
        if adicionar.validate_on_submit():

            nome = adicionar.nome.data
            email = adicionar.email.data
            senha = bcrypt.generate_password_hash(adicionar.senha.data)

            cargo = "user"            

            usuario = Usuario(nome, email, senha, cargo)

            db.session.add(usuario)
            db.session.commit()

            flash("Usuário cadastrado com sucesso!", "success")

            return redirect(url_for('principal.index'))
    else:
        flash("Este email já está sendo utilizado", "warning")

    return render_template ("adicionar.html", login=login, adicionar=adicionar, logout=logout)

@usuarios.route("/login", methods=['POST', 'GET'])
def login():

    login=LoginForm()

    if login.validate_on_submit():

        usuario = Usuario.query.filter_by(email=login.email.data).first()

        if usuario is not None:

            if usuario.check_senha(login.senha.data):

                login_user(usuario, remember=login.lembrar.data)

                next = request.args.get('next')

                if next == None or not next[0]==url_for('principal.index'):
                    next=url_for('principal.index')

                flash("Você foi logado com sucesso", "success")				
                return redirect(url_for('principal.index') )

            else:
                flash("Email e/ou senha incorretos", "danger")
        else:
            flash("Email e/ou senha incorretos", "danger")

    return redirect(url_for('principal.index'))


@usuarios.route('/logout', methods=['POST', 'GET'])
def logout():
	logout_user()
	return redirect(url_for('principal.index'))
