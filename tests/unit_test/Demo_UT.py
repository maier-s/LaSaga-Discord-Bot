from samples.Demo import Demo_Component
import unittest

class Demo_UT(unittest.TestCase):
    def test_Constructor(self):
        self.assertEqual(Demo_Component().var,1)
    def test_firstFunction(self):
        self.assertEqual(Demo_Component().firstFunction(),2)
    def test_secondFunction(self):
        def stub_firstFunction(self)->int:
            return 5
        origin_secondFunction = Demo_Component.firstFunction
        try:
            Demo_Component.firstFunction = stub_firstFunction
            self.assertEqual(Demo_Component().secondFunction(5),10)
        finally:
            Demo_Component.firstFunction = origin_secondFunction
    
if __name__ == "__main__":
    unittest.main()