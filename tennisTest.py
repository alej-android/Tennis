import unittest


class TestTennis(unittest.TestCase):
	
    def setUp(self):
        self.prueba = Tennis()
	
	def test_imprimir_puntuaje(self);
		self.assertEqual([0,0], self.imprimir_puntuaje())

if __name__=="__main__":
    unittest.main()
