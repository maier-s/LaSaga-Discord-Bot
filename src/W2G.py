import requests
from dotenv import load_dotenv
import os
class W2G:
    W2G_TOKEN = None
    URL = "https://w2g.tv/rooms/create.json"
    def __init__(self,Token=None) -> None:
        print("Congratulation you use Watch2gether Class from LaSaga Bot")
        if Token == None:
            print("No Token assigend")
            self.__del__()
        else:
            self.W2G_TOKEN = Token

    def makeRoom(self,url:str)->str:
        if url == None:
            return None # make error handling
        req = {
                       'w2g_api_key': self.W2G_TOKEN, 
                       'share': url,
            }
        response = requests.post(url=self.URL,data=headers).json()['streamkey']
        return f'https://w2g.tv/rooms/{response}'

if __name__ == "__main__":
    load_dotenv()
    W2G_TOKEN = os.getenv('W2G_TOKEN')
    test = W2G(Token=W2G_TOKEN)
    test.getRoom()
    print("Hallo Welt")