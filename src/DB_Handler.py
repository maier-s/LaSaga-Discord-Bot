# This is an DB Handler for Postgres SQL Database

import psycopg2

class DB_Handler:
    DB_Connection = None
    DB_Cursor = None
    def __init__(self):
        try:
            self.DB_Connection = psycopg2.connect("dbname='Users' host='localhost'")
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
            
            


if __name__ == "__main__":
    DB = DB_Handler()
    DB.createDatabase()