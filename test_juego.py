import unittest
from juego import compararOpciones

class TestCompararOpciones(unittest.TestCase):
    
#empate
    def testPiedra_Piedra(self):
        self.assertEqual(compararOpciones('piedra', 'piedra'), 0)

    def testPapel_Papel(self):
        self.assertEqual(compararOpciones('papel', 'papel'), 0)

    def testTijera_Tijera(self):
        self.assertEqual(compararOpciones('agua', 'tijera'), 0)

# primero gana
    def testPiedra_Tijera(self):
        self.assertEqual(compararOpciones('piedra', 'tijera'), 1)

    def testPapel_Piedra(self):
        self.assertEqual(compararOpciones('papel', 'roca'), 1)

    def testTijera_Papel(self):
        self.assertEqual(compararOpciones('tijera', 'papel'), 1)

#pierde primera opción
    def testPiedra_Papel(self):
        self.assertEqual(compararOpciones('piedra', 'papel'), -1)

    def testPapel_Tijera(self):
        self.assertEqual(compararOpciones('papel', 'tijera'), -1)

    def testTijeraPiedra(self):
        self.assertEqual(compararOpciones('tijera', 'piedra'), -1)

if __name__ == '__main__':
    unittest.main()