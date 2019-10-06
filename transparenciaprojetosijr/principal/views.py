from flask import Blueprint, render_template, redirect, flash, request, abort, url_for
from transparenciaprojetosijr.usuarios.forms import LoginForm, AdicionarUserForm, LogoutForm

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