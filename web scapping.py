import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
  
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        
        books.append({
            'Title': title,
            'Price': price,
            'Availability': availability
        })

    
    df = pd.DataFrame(books)

  
    df.to_csv('books.csv', index=False)
    print("Data saved to books.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")