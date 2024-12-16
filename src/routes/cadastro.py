from flask import render_template, request
from . import cadastro_blueprint


@cadastro_blueprint.route('/cadastro', methods=['GET','POST'])
def cadastro_cliente():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        cnpj = request.form.get("cnpj")
        ie = request.form.get("ie")
        print(f"nome: {nome},\n cpf: {cpf}, \n cnpj: {cnpj}, \n ie: {ie}")
    
    return render_template("cadastro_cliente.html")