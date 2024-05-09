import sqlite3

def init_database():
        connection = sqlite3.connect('file.db')
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ebay(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        price text,
        link text                  
 )""")
        connection.commit()
        connection.close()

def add(name, price, link):
        connection = sqlite3.connect('file.db')
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO Ebay(name,
        price,
        link)VALUES(?,?,?)""",(name, price, link ))
        connection.commit()
        connection.close()

