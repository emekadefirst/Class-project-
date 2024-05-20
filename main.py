import sqlite3


def create_database():
    connection = sqlite3.connect('file.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
                    id INTEGER PRIMARY KEY, 
                    food_name TEXT,
                    img TEXT, 
                    url TEXT, 
                    recipe_description TEXT)''')
    connection.commit()
    connection.close()



def insert_data(name, img, url, description):
    connection = sqlite3.connect('file.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Recipes VALUES(?, ?, ?, ?)",name, img, url, description)
    connection.commit()
    connection.close()
    return "Recipe saved"
