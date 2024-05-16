import requests
from bs4 import BeautifulSoup
from main import create_database, insert_data


base_url = "https://www.foodnetwork.com/recipes/photos/graduation-party-food-ideas"
n = range(1, 24)

for num in n:
    url = f"{base_url}{num}"
    response = requests.get (url)  
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for data in soup.find_all('div', {'class': 'slide'}  ):
        food_name = data.find('h2', {'class': "slide-title"})
        name = food_name.text.strip()
        recipe_description = data.find('div', {'class': "slide-caption"}) 
        description =  recipe_description.text.strip()
        img = data.find('img')['src']
        url = data.find('a')['href']
        
print(create_database(), insert_data(name, img, url, description))