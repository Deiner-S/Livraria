from flask import render_template, request
from . import login_blueprint

@login_blueprint.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':#definir metodo de recepção de dados 
        #processando os dados do formulário
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Login efetuado com usuário {username}") 

    
    return render_template('login.html')