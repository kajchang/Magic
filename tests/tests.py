import unittest
from st4ck.__main__ import main
import json


class Test_St4ck(unittest.TestCase):
        def test_scraping(self):
                main('-f data.json -a 5 -v'.split())
                with open('data.json') as file:
                        data = json.load(file)
                self.assertEqual(len(data), 5)

if __name__ == '__main__':
        unittest.main()
