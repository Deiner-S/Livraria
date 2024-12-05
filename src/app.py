from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_proteger_o_formulario'
# As classes LoginForm e CadastroForm são definidas no Python, 
# onde você especifica os campos do formulário (como username, password, nome, email) e as validações.

# Definindo uma classe de formulário usando WTForms
class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[InputRequired()])
    password = PasswordField('Senha', validators=[InputRequired()])
    submit = SubmitField('Entrar')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    submit = SubmitField('Cadastrar')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Lógica de login (processar o formulário)
        username = form.username.data
        password = form.password.data
        return f"Login feito com usuário: {username}"
    return render_template('formulario.html', form=form, form_type='login')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        # Lógica de cadastro (processar o formulário)
        nome = form.nome.data
        email = form.email.data
        return f"Cadastro realizado para: {nome}"
    return render_template('formulario.html', form=form, form_type='cadastro')

if __name__ == '__main__':
    app.run(debug=True)
