from flask import render_template, request, redirect, url_for, session
from flask_login import login_manager, login_user, current_user
from models.User import User



from . import login_bp



@login_bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('home'))  # Redireciona para o painel se já estiver logado
    
    if request.method == 'POST':#definir metodo de recepção de dados 
        #processando os dados do formulário
        username = request.form.get("username")
        password = request.form.get("password")
        authentic = User.authenticate(username, password)
        
        if authentic:
            login_user(authentic)
            return redirect(url_for('home'))
        else:
            return "Invalid credentials", 401       


    
    return render_template('login.html')




