class Nota_fiscal():
    def __init__(self,acesso,cfop):
        self._id = None
        self._acesso = acesso
        self._cfop = cfop

    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_acesso(self):
        return self._acesso
    def set_acesso(self, new):
        self._acesso = new
    
    def get_cfop(self):
        return self._cfop
    def set_cfop(self, new):
        self._cfop = new

    def values():
        return "(:cfop,:acesso)"