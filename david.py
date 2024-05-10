import requests
from bs4 import BeautifulSoup
import sqlite3

def init():
    connection = sqlite3.connect('file.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tech_blog_db(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        head text,
        link text,
        image text )""")
    
    connection.commit()
    connection.close()

def add(head, link, img):
    connection = sqlite3.connect('file.db')
    cursor = connection.cursor()
    cursor.execute("""
INSERT INTO tech_blog_db(head, link, image) VALUES(?,?,?)""",(head, link, img))
    connection.commit()
    connection.close()
url = 'https://www.engadget.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for data in soup.find_all('article', {'data-component': 'PostCard'}):
    head = data.find('a')
    heading = head.get('title')
    if heading:
        heading = heading

    else:
        headinng = "Title not found"
    
    link = data.find('a')
    linked = link.get('href')

    img_url = data.find('img')
    image = img_url.get('src')

    init()
    add(heading, linked, image)

    
    