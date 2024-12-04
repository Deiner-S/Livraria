#necessário aplicar design patern que permite uma unica instancia desse objeto
class Carrinho():    
    def __init__(self,id_cliente):
        self._id = None
        self._livros = {}
        self._finalizado = None
        self._id_cliente = id_cliente

    def get_finalizado(self):
        return self._finalizado
    def set_finalizado(self, new):
        self._finalizado = new    

    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_id_cliente(self):
        return self._id_cliente
    def set_id_cliente(self, new):
        self._id_cliente = new

    def get_livros(self):
        return self._livros
    def add_livros(self,livro,id):
        self._livros.update({id:[livro]})
    def addMais1(self,id):
        self._livros.get(id).append(self._livro.get(id)[0])

    def values():
        return "(:fk_cliente_id,:fk_livro_id,:exemplares)"

        