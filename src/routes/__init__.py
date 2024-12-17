# routes/__init__.py
from flask import Blueprint

# Inicializando Blueprints
home_blueprint = Blueprint('home', __name__)
login_blueprint = Blueprint('login', __name__)
cadastro_blueprint = Blueprint('cadastro', __name__)
logout_blueprint = Blueprint('logout', __name__)
cadastro_atendente_blueprint = ('cadatro_atendente', __name__)

# Funções para registrar as rotas nos Blueprints
from .home import *
from .login import *
from .cadastro import *
from .cadastro_atendente import *