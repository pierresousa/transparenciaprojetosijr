from flask import Blueprint, render_template, redirect, flash, request, abort, url_for, redirect
from transparenciaprojetosijr.usuarios.forms import LoginForm, AdicionarUserForm, LogoutForm
from transparenciaprojetosijr.principal.forms import AdicionarEmailForm, EscolhaJornalForm
from transparenciaprojetosijr.principal.models import Emails
from transparenciaprojetosijr import db, mail
from transparenciaprojetosijr.projetos.models import Projetos
from flask_mail import Message

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

@principal.route("/jornal", methods=['POST', 'GET'])
def jornal():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()

    return render_template("jornal.html", login=login, adicionarUser=adicionarUser, 
                            logout=logout)


@principal.route("/enviarjornal", methods=['POST', 'GET'])
def enviarJornal():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()
    escolhaJornal = EscolhaJornalForm()
    escolhas=[]
    allProjetos = Projetos.query.all()
    check = False

    for projeto in allProjetos:
        if escolhas:        
            for escolha in escolhas:
                if projeto.data_criacao == escolha[0]:
                    check=True
            if check==False:
                escolhas.append((projeto.data_criacao,projeto.data_criacao))

        else:
            escolhas.append((projeto.data_criacao,projeto.data_criacao))
    
    escolhaJornal.jornal.choices = escolhas
    if escolhas:
        if escolhaJornal.submit.data:
            projetos = Projetos.query.filter(Projetos.data_criacao.contains(escolhaJornal.jornal.data))
        
            all_emails = Emails.query.all()
            for email_ in all_emails:
                msg = Message("Transparência Ijr - Atualização de Projetos", sender="transparencia@ijunior.com.br", recipients=[email_.email])
                msg.html = render_template('jornaltemplate.html',projetos=projetos)
                mail.send(msg)
            
            flash("Email enviado com sucesso","success")
            return redirect(url_for('principal.index'))
    else:
        flash("Não há atualizações de projetos cadastrados.","warning")

    return render_template("enviarJornal.html", login=login, adicionarUser=adicionarUser, 
                            logout=logout, escolhaJornal=escolhaJornal)