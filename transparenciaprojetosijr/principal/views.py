from flask import Blueprint, render_template, redirect, flash, request, abort, url_for
from transparenciaprojetosijr.usuarios.forms import LoginForm, AdicionarUserForm, LogoutForm
from transparenciaprojetosijr.principal.forms import AdicionarEmailForm
from transparenciaprojetosijr.principal.models import Emails
from transparenciaprojetosijr import db

principal = Blueprint('principal', __name__, template_folder='templates')

@principal.route("/")
def index():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()

    return render_template("index.html", login=login, adicionarUser=adicionarUser, logout=logout)

@principal.route("/controle")
def controle():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()

    return render_template("controle.html", login=login, adicionarUser=adicionarUser, logout=logout)


@principal.route("/emails", methods=['POST', 'GET'])
def email():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()
    emailform = AdicionarEmailForm()

    email_encontrado = False

    if emailform.validate_on_submit():
        buscaemail = Emails.query.all()
        formEmail = str(emailform.email.data)
        for verEmail in buscaemail:
            comp_email = str(verEmail.email)
            if comp_email == formEmail:
                email_encontrado = True

        if not email_encontrado:
            adicionaemail = Emails(emailform.email.data)
            db.session.add(adicionaemail)
            db.session.commit()
            flash("Email cadastrado com sucesso", "success")				

        else:
            flash("Email já cadastrado", "warning")

    allEmails = Emails.query.order_by(Emails.email.asc())

    return render_template("emails.html", login=login, adicionarUser=adicionarUser, 
                            logout=logout, emailform=emailform, allEmails=allEmails)

@principal.route('/excluir_email/<int:email_id>', methods=['POST', 'GET'])
def excluir_email(email_id):

    id = email_id
    emaildelete = Emails.query.get_or_404(id)

    db.session.delete(emaildelete)
    db.session.commit()

    return redirect(url_for('principal.email'))