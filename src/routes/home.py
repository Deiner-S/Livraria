from DAO.DAO_Livro import DAO_Livro
import services.adicionar_carrinho as cart
from flask import render_template, request
from . import home_bp

@home_bp.route('/', methods=['GET','POST'])
def catalogo():
    # Conectar ao banco de dados e obter os livros
    dao_livro = DAO_Livro()    
    livros = dao_livro.read_all()
    dao_livro.close()

    if request.method == "POST":        
        isbn=request.form.get("isbn")

        cart.adicionar(isbn,id_cliente,1)

        

    # Passar os dados dos livros para o template
    return render_template('home.html', livros=livros)