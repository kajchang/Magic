import unittest
from st4ck.__main__ import main
import json
import io
from contextlib import redirect_stdout
import os


class Test_St4ck(unittest.TestCase):
    def test_scraping(self):
        main('-f data.json'.split())

        with open('data.json') as file:
            data = json.load(file)

        self.assertEqual(len(data), 1)

        os.remove('data.json')

    def test_verbose(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            main('-f data.json -v'.split())
            output = buf.getvalue().split('\n')

        output = output[:-1]

        self.assertTrue(all(line.startswith('Scraping') for line in output[:-1]))
        self.assertTrue(output[-1].startswith('Finished at'))

        os.remove('data.json')

    def test_multiple(self):
        main('-f data.json -n 5'.split())

        with open('data.json') as file:
            data = json.load(file)

        self.assertEqual(len(data), 5)

        os.remove('data.json')

    def test_targeted(self):
        main('-f data.json -id kachangred'.split())

        with open('data.json') as file:
            data = json.load(file)

        self.assertDictEqual(data[0], {'kachang': 12, '夜勤病栋': 51, '~Coral•Sea~': 321, 'Dark Zone': 1325, 'St4ck': 2802})

        os.remove('data.json')

if __name__ == '__main__':
    unittest.main()
