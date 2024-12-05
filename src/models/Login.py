class Login():
    def __init__(self,login,senha,id_atendente,ativo,data_criacao,ultimo_login):
        self._id = None
        self._id_atendente = id_atendente
        self._ativo = ativo
        self._data_criacao = data_criacao
        self._ultimo_login = ultimo_login
        self._senha = senha
        self._login = login
        

    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_login(self):
        return self._login
    def set_login(self, new):
        self._login = new
    
    def get_senha(self):
        return self._senha
    def set_senha(self, new):
        self._senha = new
    
    def get_id_atendente(self):
        return self._id_atendente
    def set_id_atendente(self, new):
        self._id_atendente = new

    def get_ativo(self):
        return self._ativo
    def set_ativo(self, new):
        self._ativo = new

    def get_data_criacao(self):
        return self._data_criacao
    def set_data_criacao(self, new):
        self._data_criacao = new
    
    def get_ultimo_login(self):
        return self._ultimo_login
    def set_ultimo_login(self, new):
        self._ultimo_login = new
    
    def values():
        return "(:fk_atendente_id,:ativo,:data_criacao,:ultimo_login,:senha,:login)"
        