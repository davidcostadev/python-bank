class Historico:
    def __init__(self):
        self.transacoes = []

    def add_transacao(self, tipo, valor):
        self.transacoes.append({'tipo': tipo, 'valor': valor})
 
