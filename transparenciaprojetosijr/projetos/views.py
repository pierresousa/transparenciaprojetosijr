from flask import Blueprint, render_template, redirect, flash, request, abort, url_for, request
from transparenciaprojetosijr.usuarios.forms import LoginForm, AdicionarUserForm, LogoutForm
from transparenciaprojetosijr.projetos.forms import AdicionarProjetoForm, AdicionarAtividadeForm
from transparenciaprojetosijr.projetos.models import Projetos, Semana, Atividades
from transparenciaprojetosijr import db
from datetime import datetime

projetos = Blueprint('projetos', __name__, template_folder='templates/projetos')

@projetos.route("/todosprojetos")
def todos_projetos():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()
    adicionarProjeto = AdicionarProjetoForm()

    allProjetos = Projetos.query.all()

    return render_template("todos_projetos.html", login=login, adicionarUser=adicionarUser, logout=logout, adicionarProjeto=adicionarProjeto, allProjetos=allProjetos)

@projetos.route("/todasatividades")
def todas_atividades():
    login = LoginForm()
    adicionarUser = AdicionarUserForm()
    logout = LogoutForm()
    adicionarAtividade = AdicionarAtividadeForm()

    atividades = Atividades.query.all()

    return render_template("todas_atividades.html", login=login, adicionarUser=adicionarUser, logout=logout, atividades=atividades, adicionarAtividade=adicionarAtividade)


@projetos.route("/adicionar", methods=['POST', 'GET'])
def adicionar():
    adicionarProjeto = AdicionarProjetoForm()

    if adicionarProjeto.validate_on_submit():
        
        projeto = Projetos(adicionarProjeto.nome.data, adicionarProjeto.descricao.data)
        data = datetime.today()
        compare_data = data.strftime("%Y-%m-%d")
        semanas = Semana.query.all()
        confirma = False
        for semana in semanas:
            data_comp = semana.data.strftime("%Y-%m-%d")
            if(data_comp == compare_data):
               confirma = True

        if not confirma:
            nova_semana = Semana(1,datetime.today())
            db.session.add(nova_semana)
        else:
            semana.quantidade = semana.quantidade+1
        
        db.session.add(projeto)
        db.session.commit()

        flash("Atualização de projeto feita com sucesso.", "success")
    return redirect(url_for('projetos.todos_projetos'))

@projetos.route("/adicionarAtividade", methods=['POST', 'GET'])
def addAtividade():
    adicionarAtividade = AdicionarAtividadeForm()

    if adicionarAtividade.validate_on_submit():
        
        atividade = Atividades(adicionarAtividade.nome.data, adicionarAtividade.descricao.data)
        db.session.add(atividade)
        db.session.commit()

        flash("Atualização de atividade feita com sucesso.", "success")
    return redirect(url_for('projetos.todas_atividades'))


@projetos.route('/excluir_projeto/<int:projeto_id>', methods=['POST', 'GET'])
def excluir_projeto(projeto_id):

    id = projeto_id
    projetodelete = Projetos.query.get_or_404(id)

    db.session.delete(projetodelete)
    db.session.commit()

    return redirect(url_for('projetos.todos_projetos'))


@projetos.route('/excluir_atividade/<int:atividade_id>', methods=['POST', 'GET'])
def excluir_atividade(atividade_id):

    id = atividade_id
    atividadedelete = Atividades.query.get_or_404(id)

    db.session.delete(atividadedelete)
    db.session.commit()

    return redirect(url_for('projetos.todas_atividades'))
