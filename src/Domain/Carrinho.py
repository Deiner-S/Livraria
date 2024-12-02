#necessário aplicar design patern que permite uma unica instancia desse objeto
class Carrinho():
    _livros = {}
    _finalizado = False
    
    def __init__(self,id,clienteId):
        self._id = id
        self._clienteId = clienteId

    def get_finalizado(self):
        return self._finalizado
    def set_finalizado(self, new):
        self._finalizado = new    

    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_clienteId(self):
        return self._clienteId
    def set_clienteId(self, new):
        self._clienteId = new

    def get_livros(self):
        return self._livros
    def add_livros(self,livro,id):
        self._livros.update({id:[livro]})
    def addMais1(self,id):
        self._livros.get(id).append(self._livro.get(id)[0])
    

        