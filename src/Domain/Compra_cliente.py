class Compra_cliente():
    def __init__(self,id,clienteId,notaFiscalId,atendenteId,data,operacao,desconto,total):
        self._id = id
        self._clienteId = clienteId
        self._notaFiscalId = notaFiscalId
        self._atendenteId = atendenteId
        self._data = data
        self._operacao = operacao
        self._desconto = desconto
        self._total = total
    
    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_clienteId(self):
        return self._clienteId
    def set_clienteId(self, new):
        self._clienteId = new

    def getnotaFiscalId(self):
        return self.notaFiscalId
    def setnotaFiscalId(self, new):
        self.notaFiscalId = new

    def getatendenteId(self):
        return self.atendenteId
    def setatendenteId(self, new):
        self.atendenteId = new

    def get_data(self):
        return self._data
    def set_data(self, new):
        self._data = new
    
    def get_operacao(self):
        return self._operacao
    def set_operacao(self, new):
        self._operacao = new

    def get_desconto(self):
        return self._desconto
    def set_desconto(self, new):
        self._desconto = new

    def get_total(self):
        return self._total
    def set_total(self, new):
        self._total = new