import sys
sys.path.append("..")

import unittest
from run import main
import json
import io
from contextlib import redirect_stdout
import os


class Test_St4ck(unittest.TestCase):
    def test_scraping(self):
        main('-f data.json'.split())

        with open('data.json') as file_:
            data = json.load(file_)

        self.assertEqual(len(data), 1)

        os.remove('data.json')

    def test_verbose(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            main('-f data.json -v'.split())
            output = buf.getvalue().split('\n')

        output = output[:-1]

        self.assertTrue(all(line.startswith('Scraping')
                            for line in output[:-1]))
        self.assertTrue(output[-1].startswith('Finished at'))

        os.remove('data.json')

    def test_multiple(self):
        main('-f data.json -n 5'.split())

        with open('data.json') as file_:
            data = json.load(file_)

        self.assertEqual(len(data), 5)

        os.remove('data.json')

    #def test_targeted(self):
    #    main('-f data.json -id kachangred'.split())
    #
    #    with open('data.json') as file_:
    #        data = json.load(file_)
    #
    #    main('-f data1.json -id 76561198045813683'.split())
    #
    #    with open('data.json') as file_:
    #        data1 = json.load(file_)
    #
    #    self.assertDictEqual(data[0], data1[0])
    #
    #    os.remove('data.json')
    #    os.remove('data1.json')


if __name__ == '__main__':
    unittest.main()
