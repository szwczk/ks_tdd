import unittest
import moj_program

class Test1TDD(unittest.TestCase):
    def test_100(self):
        wynik = moj_program.zwroc_100()
        self.assertEqual(100, wynik)
    def test_zwroc_parametr(self):
        ret = moj_program.zwroc_parametr('olek')
        self.assertEqual(ret,'olek')

if __name__ == '_main_':
    unittest.main()
