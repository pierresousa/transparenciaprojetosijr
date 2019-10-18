import os
from functools import wraps
from flask import Flask, render_template, redirect, flash, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_mail import Mail

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

############################################################
######################## EMAIL #############################
############################################################

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME'] = 'transparencia@ijunior.com.br'
app.config['MAIL_PASSWORD'] = 'atualizacaoijr'

mail = Mail(app)


############################################################
################## BANCO DE DADOS ##########################
############################################################

"""basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
"""

app.config['SQLALCHEMY_DATABASE_URI'] =  "mysql+pymysql://projetosijr:ijrprojects@projetosijr.mysql.dbaas.com.br/projetosijr"
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 300
app.config['SQLALCHEMY_POOL_RECYCLE'] = 30
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#############################################################
################## CONFIGURA LOGIN ##########################
#############################################################

login_manager.init_app(app)
login_manager.login_view = "principal.index"

def login_required(role=["ANY"]):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):

            if not current_user.is_authenticated:
               return current_app.login_manager.unauthorized()
            urole = current_user.get_urole()
            if ( (urole not in role) and (role != ["ANY"])):
                return current_app.login_manager.unauthorized()      
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

#############################################################
####################### BLUEPRINTS ##########################
#############################################################

from transparenciaprojetosijr.usuarios.views import usuarios
from transparenciaprojetosijr.projetos.views import projetos
from transparenciaprojetosijr.principal.views import principal
from transparenciaprojetosijr.error_pages.handlers import error_pages


app.register_blueprint(usuarios,url_prefix='/usuarios')
app.register_blueprint(projetos,url_prefix='/projetos')
app.register_blueprint(principal)
app.register_blueprint(error_pages)

####################################
############FUNÇÕES#################
####################################
	

@app.template_filter('converte')
def converte(data):
    return data.strftime("%Y-%m-%d")
