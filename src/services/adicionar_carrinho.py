import util.Util as u

from models.Livro import Livro
from DAO.DAO_Livro import DAO_Livro

from models.Cliente import Cliente
from DAO.DAO_Cliente import DAO_Cliente

from models.Carrinho import Carrinho
from DAO.DAO_Carrinho import DAO_Carrinho


def adicionar(id_livro,id_cliente,exemplar):
    #procurar cliente no banco
    #se encontrar instancie objeto cliente
    #se não cadastre cliente
    dao_cliente = DAO_Cliente()
    dados_cliente = dao_cliente.read(id_cliente)
    cliente = Cliente(*dao_cliente)
    dao_cliente.close()

    dao_livro = DAO_Livro()
    dados_livro = dao_livro.read(id_livro)
    livro = Livro(*dao_livro)
    dao_livro.close()
    
    
    
    dao_carrinho = DAO_Carrinho()
    #retorna uma lista com o id de carrinho ativo e seus itens
    carrinho_existente = dao_carrinho.read_cliente(id_cliente)
    #verifica se tem um carrinho ativo
    if carrinho_existente != []:
        for i in carrinho_existente:
            #verifica se no carrinho ativo comtem o livro a ser adicionado
            if i[2] == id_livro:
                i[2] = i[2]+1
                carrinho = Carrinho(*i)
                dao_carrinho.update(carrinho)
                break
            #se não adiciona livro ao carrinho existente
            else:
                carrinho = Carrinho(carrinho_existente[0][0],id_cliente,id_livro,exemplar)
                dao_carrinho.create(carrinho)
    #se não cria novo carrinho e adiciona primeiro livro do carrinho 
    else:
        id_carrinho = u.id_numerico()
        carrinho = Carrinho(id_carrinho,id_cliente,id_livro,exemplar)
        dao_carrinho.create(carrinho)


    dao_carrinho.close()
