import requests
from bs4 import BeautifulSoup
import sqlite3
def create():
    connection = sqlite3.connect('file.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sports (
                        id INTEGER PRIMARY KEY,
                        header TEXT,
                        link TEXT,
                        ima TEXT)''')
    connection.commit()
    connection.close()
    
def add_data(header, link, image):
    connection = sqlite3.connect('file.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO sports(header,link, ima ) VALUES (?,?,?) ",(header, link, image))
    
    connection.commit()
    connection.close()
    


url = 'https://punchng.com/topics/sports/'
response = requests.get(url)
if response.status_code ==200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    for data in soup.find_all('article'):
        
        
        header = data.find('h1', {'class': 'post-title'})
        head = header
            
            
        link = data.find('a')['href']
        
        img = data.find('img', {'class': 'post-image'})

        create()
        add_data(head, link, img)
    # print(header.text.strip())
    # print(data)
# print(soup)