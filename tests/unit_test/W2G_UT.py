import sys
import os
from unittest.case import TestCase
sys.path.append(os.getcwd()+"/src") #assuming that unit test is executed from main directory
from W2G import W2G
import unittest
import requests


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
        self.assertEqual(isinstance(self.uut, W2G),True)
        self.assertEqual(self.uut.W2G_TOKEN,None)
    def test_W2G_makeRoom(self):
        self.uut = W2G("UT")
        #Stub Post function with custom code 
        # Implement .json() function that function can use 
        class stub_request_response:
            response = {"streamkey":"UT"}
            def __init__(self):
                pass
            def json(self):
                return self.response
        def stub_request_post(url = None, data = None):
            return stub_request_response()
        origin_function_request_post = requests.post
        try:
            requests.post = stub_request_post
            self.assertEqual(self.uut.makeRoom(url = "Test")[0],"https://w2g.tv/rooms/UT")
        finally:
            requests.post = origin_function_request_post

        



if __name__ == "__main__":
    unittest.main()
    