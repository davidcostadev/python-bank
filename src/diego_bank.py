class Historico:
    def __init__(self):
        self.transacoes = []

    def add_transacao(self, tipo, valor):
        
        if valor <= 0:
            raise Exception('Error: O valor precisa ser maior do que zero.')
        elif tipo != 'saque' and tipo != 'deposito':
             raise Exception('Error: Tipo inválido. Precisa ser "saque" ou "deposito"')
        else:
            self.transacoes.append({'tipo': tipo, 'valor': valor})

    def get_transacoes(self):
        return self.transacoes
        