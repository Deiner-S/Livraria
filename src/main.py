from flask import Flask
from flask_login import LoginManager
from routes import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'AB3lh4_60sta_d3_m3l'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)   

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(auth_bp)
#app.register_blueprint(logout_blueprint)
#app.register_blueprint(cadastro_atendente_blueprint)

if __name__ == '__main__':
    app.run(debug=True)