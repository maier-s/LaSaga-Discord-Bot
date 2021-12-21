class Demo_Component:
    var = 0
    def __init__(self):
        self.var = 1
    def firstFunction(self)->int:
        return 2
    def secondFunction(self, number:int)->int:
        return self.firstFunction() + number