import unittest
from baseball import function1, function2


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(getList({"brand": "Ford","model": "Mustang","year": 1964}), ['brand', 'model', 'year'])

    def test_function2(self):
        self.assertEqual(createAPIData("http://api.open-notify.org/astros.json"), '{"number": 10, "people": [{"name": "Oleg Artemyev", "craft": "ISS"}, {"name": "Denis Matveev", "craft": "ISS"}, {"name": "Sergey Korsakov", "craft": "ISS"}, {"name": "Kjell Lindgren", "craft": "ISS"}, {"name": "Bob Hines", "craft": "ISS"}, {"name": "Samantha Cristoforetti", "craft": "ISS"}, {"name": "Jessica Watkins", "craft": "ISS"}, {"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}], "message": "success"}')

if __name__ == '__main__':
    unittest.main()