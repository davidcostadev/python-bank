from src.exemplo import Exemplo
import unittest

class ExemploTest(unittest.TestCase):
    def test_soma(self):
        """Deve soma 2 elementos"""
        exemplo = Exemplo()
        resultado = exemplo.soma(1, 2)

        self.assertEqual(resultado, 3)





if __name__ == '__main__':
    unittest.main()