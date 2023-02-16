## instal pyodbc ----> pip install pyodbc
import pyodbc 

try:
    cnxn = pyodbc.connect('DRIVER={SQL Server};Server=DESKTOP-P3OGUBB\SQLEXPRESS;Database=HangmanGame;Trusted_Connection=yes')
    print("funciono")
    cursor = cnxn.cursor()
    listPlayer = []

    cursor.execute("SELECT TOP 10 * FROM Players order by 3 DESC") 
    row = cursor.fetchone() 
    

    def createPlayer(name, score):
         cursor.execute(f"INSERT INTO Players VALUES ('{name}', {score})")
         cursor.commit()
 
    
    while row:
        print (row)
        listPlayer.append(row)
        row = cursor.fetchone()


    def getList():
        return listPlayer        
       
    cursor.close()
    
except Exception as ex:
    print(ex)
    