import sqlite3

connection = sqlite3.connect('file.db')

cursor = connection.cursor()


connection.close()