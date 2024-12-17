from flask import render_template, request, redirect, url_for, session
from DAO.DAO_Login import DAO_Login


from . import login_blueprint
from . import logout_blueprint

@login_blueprint.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':#definir metodo de recepção de dados 
        #processando os dados do formulário
        username = request.form.get("username")
        password = request.form.get("password")
        dao_login = DAO_Login()
        login = dao_login.read(username)
        dao_login.close()
        if login != None:
            for i in login:
                if i[2]:
                    valor = i[6] == password
                    if valor:
                        session['usuario'] = username
                        return redirect(url_for('home'))
                    else:
                        return "usuário ou senha incorretos", 401    
        else:
            return "usuário ou senha incorretos", 401


    
    return render_template('login.html')

@logout_blueprint.route('/logout')
def logout():
    session.pop('usuario', None)  # Remover o usuário da sessão
    return redirect(url_for('login'))