## instal pyodbc ----> pip install pyodbc
import pyodbc 

class Db_conector:
    
        def __init__(self):
            try:
                self.cnxn = pyodbc.connect('DRIVER={SQL Server};Server=DESKTOP-P3OGUBB\SQLEXPRESS;Database=HangmanGame;Trusted_Connection=yes')
                self.cursor = self.cnxn.cursor()
                self.listPlayer = []

                self.cursor.execute("SELECT TOP 6 * FROM Players order by 3 DESC") 
                self.row = self.cursor.fetchone()
            
                while self.row:  
                    self.listPlayer.append(self.row)
                    self.row = self.cursor.fetchone()
            except Exception as ex:
                print(ex)

        def createPlayer(name, score, self):
            self.cursor.execute(f"INSERT INTO Players VALUES ('{name}', {score})")
            self.cursor.commit()
 
        def getList(self):
            self.cursor.close()
            return self.listPlayer        

        
    
    