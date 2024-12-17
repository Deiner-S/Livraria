from flask import render_template, request
from . import cadastro_blueprint


@cadastro_blueprint.route('/cadastro', methods=['GET','POST'])
def cadastro_cliente():
    if request.method == "POST":
        nome = request.form.get("nome")
        email =request.form.get("email")       
        senha = request.form.get("senha")
        print(f"nome: {nome},\n cpf: {cpf}, \n cnpj: {cnpj}, \n ie: {ie}")
    
    return render_template("cadastro_cliente.html")