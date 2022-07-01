import unittest
import baseball


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(getList({"brand": "Ford","model": "Mustang","year": 1964}), ['brand', 'model', 'year'])

    def test_function2(self):
        self.assertEqual(filterDict({"brand": "Ford","model": "Mustang","year": 1964},"brand"),{"brand": "Ford"})
        
if __name__ == '__main__':
    unittest.main()