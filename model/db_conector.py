## instal pyodbc ----> pip install pyodbc
import pyodbc 

try:
    cnxn = pyodbc.connect('DRIVER={SQL Server};Server=DESKTOP-P3OGUBB\SQLEXPRESS;Database=HangmanGame;Trusted_Connection=yes')
    print("funciono")
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Players order by 3 DESC") 

    row = cursor.fetchone() 
    

    def createPlayer(name, score):
         cursor.execute(f"INSERT INTO Players VALUES ('{name}', {score})")
         cursor.commit()
    createPlayer('Santiago', 25)

    cursor.execute("SELECT * FROM Players order by 3 DESC")
    while row:
        print (row) 
        row = cursor.fetchone()
    cursor.close() 
except Exception as ex:
    print(ex)
    