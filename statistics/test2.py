import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

data = {'href': [], 'product_name': [], 'price': []}

for i in range(2, 50):
    url = f'https://wikkeo.com/latest?page={i}'
    response = requests.get(url, headers=header, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', {'class': 'product-name'})
    for product in products:
        a = product.find('a')
        href = a.get('href')
        product_name = product.text.strip()

        prices = soup.find_all('span', {'class': 'price_no_format_58'})
        price = prices[products.index(product)].text.strip()

        data['href'].append(href)
        data['product_name'].append(product_name)
        data['price'].append(price)

df = pd.DataFrame(data)
df.to_csv('produc5ts.csv', index=False)