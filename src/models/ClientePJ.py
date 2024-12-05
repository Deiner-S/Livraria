from Cliente import Cliente

class clientePJ(Cliente):    
    def __init__(self,nomeFantasia,nome,cnpj,ie):
        super().__init__(nome)
        self._nomeFantasia = nomeFantasia
        self._cnpj = cnpj
        self._ie = ie

    def get_nomeFantasia(self):
        return self._nomeFantasia
    def set_nomeFantasia(self, new):
        self._nomeFantasia = new

    def get_cnpj(self):
        return self._cnpj
    def set_cnpj(self, new):
        self._cnpj = new

    def get_ie(self):
        return self._ie
    def set_ie(self, new):
        self._ie = new
    
    def values():
        return "(:nome,:cnpj,:ie,:tipo)"


