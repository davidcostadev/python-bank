import unittest
from datetime import datetime
from src.diego_bank import Historico

class HistoricoTest(unittest.TestCase):
    def test_init_historico(self):
        """ Deve criar uma variavel transacoes com uma lista vazia"""
        historico = Historico()

        self.assertEqual(len(historico.transacoes), 0)
    
    def test_add_transacao(self):
        """ Deve adicionar uma transacao na lista """
        historico = Historico()

        self.assertEqual(len(historico.transacoes), 0)

        historico.add_transacao('saque', 10.45, '30/07/2019')

        self.assertEqual(len(historico.transacoes), 1)

        transacao = historico.transacoes[0]

        self.assertEqual(transacao, {
            'tipo': 'saque',
            'valor': 10.45,
            'data': datetime(2019, 7, 30, 0, 0)
        })
    
    def test_add_transacao_validar_valores(self):
        """ Deve dar error ao adicionar valores igual ou abaixo que zero """
        historico = Historico()
        with self.assertRaisesRegex(Exception, 'Error: O valor precisa ser maior do que zero.'): 
          historico.add_transacao('saque', 0, '30/07/2019')

        with self.assertRaisesRegex(Exception, 'Error: O valor precisa ser maior do que zero.'): 
          historico.add_transacao('saque', -1, '30/07/2019')
    
    def test_add_transacao_validar_tipos(self):
        """ Deve dar error ao adicionar transacoes com tipos invalidos """
        historico = Historico()
        with self.assertRaisesRegex(Exception, 'Error: Tipo inválido. Precisa ser "saque" ou "deposito"'): 
          historico.add_transacao('emprestimo', 100, '30/07/2019')

    def test_get_transacoes(self):
      """ Deve retornar a lista de todas as transacoes """

      historico = Historico()

      self.assertEqual(len(historico.get_transacoes()), 0)

      historico.add_transacao('saque', 10.45, '30/07/2019')
      historico.add_transacao('deposito', 100, '30/07/2019')
      historico.add_transacao('saque', 20, '30/07/2019')

      self.assertEqual(len(historico.get_transacoes()), 3)

if __name__ == '__main__':
    unittest.main()
