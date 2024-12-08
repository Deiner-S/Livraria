

class Cliente():
    def __init__(self,nome,cpf_cnpj,cliente_tipo):
        self._nome = nome
        self._cpf_cnpj= cpf_cnpj
        self._ie = None
        self._cliente_tipo = cliente_tipo
                    
    
    def get_cpf_cnpj(self):
       return self._cpf_cnpj
    def set_cpf_cnpj(self,new):
       self._cpf_cnpj = new
    
    def get_nome(self):
        return self._nome
    def set_nome(self, new):
        self._nome = new

    def get_ie(self):
       return self._ie
    def set_ie(self,new):
       self._ie= new

    def get_cliente_tipo(self):
       return self._cliente_tipo
    def set_cliente_tipo(self,new):
       self._cliente_tipo= new
      