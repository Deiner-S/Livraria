class Compra_cliente():
    def __init__(self,id_carrinho,id_notaFiscal,id_atendente,data,operacao,desconto,total):
        self._id = None
        self._id_carrinho = id_carrinho
        self._id_notaFiscal = id_notaFiscal
        self._id_atendente = id_atendente
        self._operacao = operacao
        self._data = data
        self._desconto = desconto
        self._total = total
    
    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_id_carrinho(self):
        return self._id_carrinho
    def set_id_carrinho(self, new):
        self._id_carrinho = new

    def get_id_notaFiscal(self):
        return self._id_notaFiscal
    def set_id_notaFiscal(self, new):
        self._id_notaFiscal = new

    def get_id_atendente(self):
        return self._id_atendente
    def set_id_atendente(self, new):
        self._id_atendente = new

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
    
    def values():
        return "(:fk_carrinho_id,:fk_notaFiscal_id,:fk_atendente_id,:operacao,:data,:desconto,:total)"