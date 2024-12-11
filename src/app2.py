from flask import Flask, render_template, request

from DAO.DAO_Livro import DAO_Livro

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':#definir metodo de recepção de dados 
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

@app.route('/')
def catalogo():
    # Conectar ao banco de dados e obter os livros
    dao_livro = DAO_Livro()    
    livros = dao_livro.read_all()
    dao_livro.close()

    # Passar os dados dos livros para o template
    return render_template('home.html', livros=livros)


if __name__ == '__main__':
    app.run(debug=True)