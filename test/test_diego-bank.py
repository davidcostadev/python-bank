from src.diego_bank import Historico
import unittest

class HistoricoTest(unittest.TestCase):
    def test_init_historico(self):
        """ Deve criar uma variavel transacoes com uma lista vazia"""
        historico = Historico()

        self.assertEqual(len(historico.transacoes), 0)
    
    def test_add_transacao(self):
        """ Deve adicionar uma transacao na lista """
        historico = Historico()

        self.assertEqual(len(historico.transacoes), 0)

        historico.add_transacao('saque', 10.45)

        self.assertEqual(len(historico.transacoes), 1)

        transacao = historico.transacoes[0]

        self.assertEqual(transacao, {
            'tipo': 'saque',
            'valor': 10.45
        })





if __name__ == '__main__':
    unittest.main()