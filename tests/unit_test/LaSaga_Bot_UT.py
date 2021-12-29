import sys
import os
sys.path.append(os.getcwd()+"/src") #assuming that unit test is executed from main directory
from LaSaga_Bot import LaSaga_Bot
from inspect import getmembers
import Com_Bot
import unittest
import discord

class La_Saga_UT(unittest.TestCase):
    uut = None
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.uut = LaSaga_Bot()
    
    def test_LaSaga_Bot_init(self):
        #Stub init commands function
        def stub_init_commands(self)->None:
            return None
        origin_init_command = self.uut.init_commands
        try:
            self.uut.init_commands = stub_init_commands
            # Check if Bot is an subclass of discord.ext.commands.Bot essential for the rest of the code
            self.assertEqual(isinstance(self.uut,discord.ext.commands.Bot),True)
        finally:
            self.uut.init_commands = origin_init_command
        
    
    def test_init_commands(self):
        com_functions = []
        for object in getmembers(Com_Bot):
            if type(object[1]) == discord.ext.commands.core.Command:
                com_functions.append(object[0])
        for function in com_functions:
            self.assertIsNotNone(self.uut.get_command(function))
    def test_on_ready(self):
        #Define Unit test for on ready
        pass
        
if __name__ == "__main__":
    unittest.main()