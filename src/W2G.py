import requests
from dotenv import load_dotenv
import os
class W2G:
    W2G_TOKEN = None
    URL_CREATE = "https://w2g.tv/rooms/create.json"
    def __init__(self,Token=None) -> None:
        if Token == None:
            print("No Token assigend")
            self.__del__()
        else:
            self.W2G_TOKEN = Token

    def makeRoom(self,url:str)->(str,str):
        if url == None:
            return None # make error handling
        req = {
                       'w2g_api_key': self.W2G_TOKEN, 
                       'share': url
            }
        response = requests.post(url=self.URL_CREATE,data=req).json()['streamkey']
        return (f'https://w2g.tv/rooms/{response}',response)
    def updateRoom(self,streamkey:str,url:str)->bool:
        if url == None or streamkey == None:
            return False
        req = {
                       'w2g_api_key': self.W2G_TOKEN, 
                       'item_url': url
            }
        response = requests.post(url=f'https://w2g.tv/rooms/{streamkey}/sync_update',data=req)
        if response.status_code == 200:
            return True
        else:
            return False