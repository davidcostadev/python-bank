from src.diego_bank import Historico
import unittest

class HistoricoTest(unittest.TestCase):
    def test_init_historico(self):
        """ Deve criar uma variavel transacoes com uma lista vazia"""
        historico = Historico()

        self.assertEqual(historico.transacoes, [])





if __name__ == '__main__':
    unittest.main()