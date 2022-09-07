import unittest

from challenge1 import *


class MyFirstTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(['1','1','1']), 3)


if __name__ == '__main__':
    unittest.main()
