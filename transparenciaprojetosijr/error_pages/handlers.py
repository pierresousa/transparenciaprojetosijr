from flask import Blueprint,render_template

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error_404(error):
	return "<h1>Essa página não existe</h1>" , 404

@error_pages.app_errorhandler(403)
def error_403(error):
	return "<h1>Acesso negado</h1>" , 403
