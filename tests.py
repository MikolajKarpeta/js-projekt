import unittest

from main_test import *


class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.root = interface()

    def test_1(self):
        self.assertRaises(ValueError, self.root.zmiana_czasu, "2020/10/10|10:10")

        self.root.zmiana_czasu("2030/9/18|12:34")


    def test_2(self):
        self.root.zmiana_czasu("2030/9/18|10:00")
        self.root.przycisk2zl(1)
        self.root.przycisk2zl(2)
        self.root.przycisk5zl(1)
        self.root.przycisk5zl(1)

    def test_3(self):
        self.root.zmiana_czasu("2030/9/17|18:30")
        self.root.przycisk2zl(1)
        self.root.przycisk5zl(1)

    def test_4(self):
        self.root.zmiana_czasu("2030/9/18|19:00")
        self.root.przycisk1zl(1)
        self.root.przycisk5zl(1)

    def test_5(self):
        self.root.zmiana_czasu("2030/9/18|10:00")
        self.root.przycisk1zl(1)

    def test_6(self):
        self.root.zmiana_czasu("2030/9/18|10:00")
        self.root.przycisk0_01zl(200)

    def test_7(self):
        self.root.zmiana_czasu("2030/9/18|10:00")
        self.root.przycisk0_01zl(201)

    def test_8(self):
        self.root.zmiana_czasu("2030/9/18|10:00")
        self.root.wypisanie_biletu("IOHF34")

    def test_9(self):
        self.root.zmiana_czasu("2030/9/18|10:00")
        self.root.przycisk5zl(2)
        self.root.wypisanie_biletu("f32#@")















if __name__ == '__main__':
    unittest.main()
