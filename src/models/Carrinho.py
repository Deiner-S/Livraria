class Carrinho():    
    def __init__(self,id,id_cliente,id_livro,exemplar):
        self._id = id
        self._id_cliente = id_cliente
        self._id_livro = id_livro
        self._exemplar = exemplar
        self._status = True

    def get_status(self):
        return self._status
    def set_status(self, new):
        self._status = new    

    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_id_cliente(self):
        return self._id_cliente
    def set_id_cliente(self, new):
        self._id_cliente = new

    def get_id_livro(self):
        return self._id_livro
    def set_id_livro(self, new):
        self._id_livro = new

    def get_exemplar(self):
        return self._exemplar
    def set_exemplar(self, new):
        self._exemplar = new

    

        