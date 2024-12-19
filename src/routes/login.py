from flask import render_template, request, redirect, url_for, session
from flask_login import login_manager, login_user, current_user
from models.User import User
from DAO.DAO_Login import DAO_Login


from . import login_blueprint



@login_blueprint.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('home'))  # Redireciona para o painel se já estiver logado
    
    if request.method == 'POST':#definir metodo de recepção de dados 
        #processando os dados do formulário
        username = request.form.get("username")
        password = request.form.get("password")

        dao_login = DAO_Login()
        lista_login = dao_login.read(username)
        dao_login.close() 
        

        if login != None: #se lista login for diferente de vazia percorra a lista
            for login in lista_login:
                if login[2]: #se item da lista no seu indice 2 for verdadeiro  então compare seu item 6 com a variavel password e armazene em valido 
                    valido = login[6] == password
                    if valido: #se valido for verdadeiro efetue login
                        user = User(login[0],login[1])
                        login_user(user)
                        return redirect(url_for('home'))
                    else:
                        return "usuário ou senha incorretos", 401    
        else:
            return "usuário ou senha incorretos", 401


    
    return render_template('login.html')




