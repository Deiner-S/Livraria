# routes/__init__.py
from flask import Blueprint

# Inicializando Blueprints
home_bp = Blueprint('home', __name__)
login_bp = Blueprint('login', __name__)
cadastro_bp = Blueprint('cadastro', __name__)
logout_bp = Blueprint('logout', __name__)
dashboard_bp = Blueprint('blueprint', __name__)
cadastro_atendente_bp = Blueprint('cadatro_atendente', __name__)
auth_bp = Blueprint('auth', __name__)
# Funções para registrar as rotas nos Blueprints
from .home import *
from .login import *
from .cadastro import *
from .cadastro_atendente import *