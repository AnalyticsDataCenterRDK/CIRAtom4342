from bs4 import BeautifulSoup
import pandas as pd
import requests

header = {
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X; sl-SI) AppleWebKit/531.3.1 (KHTML, like Gecko) Version/4.0.5 Mobile/8B111 Safari/6531.3.1'
}

def categories_electronics():
    url = 'https://www.avito.ru/all/bytovaya_elektronika'
    response = requests.get(url, headers=header, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    sub_content = soup.find_all('a', {'class': 'rubricator-list-item-link-uPiO2'})
    for i in sub_content:
        print(i.text)
        a = i.find('a')
        href = a.get('href')
        print('Ссылка на категорию -',href, 'Название категории -',i.text)
categories_electronics()