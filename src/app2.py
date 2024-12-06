from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #processando os dados do formulário
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Login efetuado com usuário {username}") 

    
    return render_template('login.html')



@app.route('/cadastro', methods=['GET','POST'])
def cadastro_cliente():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        cnpj = request.form.get("cnpj")
        ie = request.form.get("ie")
        print(f"nome: {nome},\n cpf: {cpf}, \n cnpj: {cnpj}, \n ie: {ie}")
    
    return render_template("cadastro_cliente.html")

if __name__ == '__main__':
    app.run(debug=True)