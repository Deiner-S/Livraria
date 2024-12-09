class Endereco():
    def __init__(self,id_cliente,cep,rua,numero,bairro,complemento,cidade,estado):
        self._id = None
        self._id_cliente = id_cliente
        self._cep = cep
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._complemento = complemento
        self._cidade = cidade
        self._estado = estado
        
    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_rua(self):
        return self._rua
    def set_rua(self, new):
        self._rua = new

    def get_numero(self):
        return self._numero
    def set_numero(self, new):
        self._numero = new

    def get_bairro(self):
        return self._bairro
    def set_bairro(self, new):
        self._bairro = new

    def get_cidade(self):
        return self._cidade
    def set_cidade(self, new):
        self._cidade = new
    
    def get_estado(self):
        return self._estado
    def set_estado(self, new):
        self._estado = new

    def get_id_cliente(self):
        return self._id_cliente
    def set_id_cliente(self, new):
        self._id_cliente = new
    
    def get_cep(self):
        return self._cep
    def set_cep(self, new):
        self._cep = new

    def get_complemento(self):
        return self._complemento
    def set_complemento(self, new):
        self._complemento = new
    
    