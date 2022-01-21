import sys
import os
from unittest.case import TestCase
sys.path.append(os.getcwd()+"/src") #assuming that unit test is executed from main directory
from W2G import W2G
import unittest

class W2G_UP(unittest.TestCase):
    uut = None

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
    def test_W2G_init_withToken(self):
        self.uut = W2G("UT")
        self.assertEqual(isinstance(self.uut, W2G),True)
        self.assertEqual(self.uut.W2G_TOKEN,"UT")
    def test_W2G_init_withoutToken(self):
        self.uut = W2G()
        self.assertEqual(isinstance(self.uut, None),True)

if __name__ == "__main__":
    unittest.main()
    