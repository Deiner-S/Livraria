from flask import redirect, url_for
from flask_login import login_required, logout_user

from . import logout_blueprint
@logout_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))