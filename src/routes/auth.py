from flask_login import login_required

from . import auth_bp

@auth_bp.route('/protected')
@login_required
def protected():
    return "Esta é uma rota protegida."