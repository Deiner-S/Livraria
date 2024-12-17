from flask import render_template, request


from . import cadastro_atendente_blueprint

@cadastro_atendente_blueprint.route('/cadastro_atendente' methods = 'POST', 'GET')
def cadastro_atendente():
    if request.method("POST"):
        request.form.get("email")
        


    return render_template("cadastro_atendente.html")