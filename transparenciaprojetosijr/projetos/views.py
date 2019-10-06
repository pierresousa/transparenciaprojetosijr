from flask import Blueprint, render_template, redirect, flash, request, abort, url_for
from transparenciaprojetosijr.usuarios.forms import LoginForm, AdicionarUserForm, LogoutForm

projetos = Blueprint('projetos', __name__, template_folder='templates/projetos')

@projetos.route("/todosprojetos")
def todos_projetos():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()
    return render_template("todos_projetos.html", login=login, adicionarUser=adicionarUser, logout=logout)

@projetos.route("/todasatividades")
def todas_atividades():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()
    return render_template("todas_atividades.html", login=login, adicionarUser=adicionarUser, logout=logout)