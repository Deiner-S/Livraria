from flask import Flask
from routes import *


app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(cadastro_blueprint)

if __name__ == '__main__':
    app.run(debug=True)