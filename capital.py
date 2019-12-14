import unittest
import upper

class Testy_litery(unittest.TestCase):
    def test_upper(self):
        font = upper.duze('jakis teks z malymi literami')
        self.assertEqual(font, 'Jakis teks z malymi literami')

    def test_foldowanie(self):
        font = upper.male('Jakas Dziwna Powiastka O Niczym')
        self.assertEqual(font, 'jakas dziwna powiastka o niczym')

    def test_upperowanie(self):
        font = upper.WIELKIE('sprawdzam jak beda wygladac literki')
        self.assertEqual(font, 'SPRAWDZAM JAK BEDA WYGLADAC LITERKI')
    def test_zmieniasie(self):
        font = upper.zmiana('sprawdzam czy sie zmieni banan')
        self.assertEqual(font, 'sprawdzam czy sie zmieni brzoskwinia')



if __name__=='__main__':
    unittest.main()
