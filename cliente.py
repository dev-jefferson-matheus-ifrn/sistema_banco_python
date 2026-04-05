class cliente:
    def __init__(self, endereco):
        self.__endereco = endereco
        self.__contas = []
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
        
    def realizar_transacao(self, conta, transacao):
        pass
    
    def adicionar_conta(self, conta):
        self.__contas.append(conta)