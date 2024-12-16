from DAO.DAO_Livro import DAO_Livro
from flask import render_template, request
from . import home_blueprint

@home_blueprint.route('/', methods=['GET','POST'])
def catalogo():
    # Conectar ao banco de dados e obter os livros
    dao_livro = DAO_Livro()    
    livros = dao_livro.read_all()
    dao_livro.close()

    if request.method == "POST":        
        isbn=request.form.get("isbn")
        titulo=request.form.get("titulo")
        autor=request.form.get("autor")
        assunto=request.form.get("assunto")
        idioma=request.form.get("idioma")
        editora=request.form.get("editora")
        estoque=request.form.get("estoque")
        preco=request.form.get("preco")

        

    # Passar os dados dos livros para o template
    return render_template('home.html', livros=livros)