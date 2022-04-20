# This is an DB Handler for Postgres SQL Database

import psycopg2
from dotenv import load_dotenv
import os

class DB_Handler:
    DB_Connection = None
    DB_Cursor = None
    def __init__(self):
        try:
            self.DB_Connection = psycopg2.connect(database='Users', host='localhost',user='postgres', password=os.getenv('DB_PASSWORD'))
            self.DB_Cursor = self.DB_Connection.cursor()

            print("Sucessfully connected to Database and created Cursor")
        
        except:
            print("ERROR: Unable to connect to Database")

    def createDatabase(self):
        table_existing = None
        try:
            self.DB_Cursor.execute("""
                SELECT EXISTS (
                SELECT FROM pg_tables
                WHERE  schemaname = 'Users'
                AND    tablename  = 'Users'
            );
            """)
            table_existing = self.DB_Cursor.fetchall()[0][0]
        except:
            print("ERROR: Cannot check if the basline Table Set exists.")

        if not table_existing and not table_existing == None:
            try:
                self.DB_Cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Users (
                        UserID serial PRIMARY KEY,
                        Discord_UserName VARCHAR(50) NOT NULL,
                        LOL_UserName VARCHAR(50) NOT NULL
                    );
                """)

            except:
                print("ERROR: Cannot Create User Table")
            self.DB_Connection.commit()
    def createLoLUser(self,DiscordUserID:str = None,LoLUserID:str = None):
        if not (self.DB_Connection == None  or self.DB_Cursor == None):
            try:
                self.DB_Cursor.execute("""
                    SELECT EXISTS (
                    SELECT FROM Users
                    WHERE Discord_UserName = %s
                );
                """,(DiscordUserID,))
                User_exists = self.DB_Cursor.fetchall()[0][0]
                if not User_exists:
                    try:
                        self.DB_Cursor.execute("""
                        INSERT INTO Users (Discord_UserName,LOL_UserName)
                        VALUES (%s,%s);
                        """, (DiscordUserID, LoLUserID))

                    except:
                        print("ERROR: Can't create User")
                else:
                    print(f'ERROR: User with Username {DiscordUserID} already exists in Database')
            except:
                print("ERROR: Cannot check if the User exists or not!")

            self.DB_Connection.commit()
        else:
            print("ERROR: Cannto execute SQL Functions because no DB Connection or Curser exists.")
    def removeUser(self,DiscordUserID:str, LoLUserID:str):
        if not (self.DB_Connection == None  or self.DB_Cursor == None):
            try:
                self.DB_Cursor.execute("""
                    SELECT EXISTS (
                    SELECT FROM Users
                    WHERE LOL_UserName = %s AND Discord_UserName =%s
                );
                """,(LoLUserID,DiscordUserID))
                User_exists = self.DB_Cursor.fetchall()[0][0]
                if User_exists:
                    try:
                        self.DB_Cursor.execute("""
                        DELETE FROM Users
                        WHERE Discord_UserName = %s AND LOL_UserName = %s;
                        """, (DiscordUserID, LoLUserID))
                        self.DB_Connection.commit()
                    except:
                        print("ERROR: Can not delete User from Table")
                else:
                    print(f'ERROR: User with Username {LoLUserID} dont exists in Database')
            except:
                print("ERROR: Cannote check if the User exists")
        else:
            print("ERROR: Cannto execute SQL Functions because no DB Connection or Curser exists.")
    def getLoLUser(self, DiscordUser:str = None)->str:
        LoL_UserID = None
        if not DiscordUser == None:
            try:
                self.DB_Cursor.execute("""
                                    SELECT LOL_UserName
                                    FROM Users
                                    WHERE Discord_UserName =%s;
                                """, (DiscordUser,))
                LoL_UserID = self.DB_Cursor.fetchall()[0][0]
            except:
                print(f'ERROR: No LoL User found for Discord User: {DiscordUser}')
        else:
            print("ERROR: No Discord User ID recieved")
        return LoL_UserID


            
            


if __name__ == "__main__":
    load_dotenv()
    DB = DB_Handler()
    DB.createDatabase()
    DB.createLoLUser("DiscordUser", "LoLUser")
    DB.createLoLUser("Test1", "Test2")
    DB.removeUser("Test1", "Test2")
    print(DB.getLoLUser("DiscordUser"))
