from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


header = {
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X; sl-SI) AppleWebKit/531.3.1 (KHTML, like Gecko) Version/4.0.5 Mobile/8B111 Safari/6531.3.1'
}


def new_item():
    url = 'https://www.ozon.ru/search/?from_global=true&text=новинки'

    response = requests.get(url, headers=header, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    prices = soup.find_all('a', class_='d6-a0')
    for i in prices:
        print(i.text)

        star = soup.find_all('span', class_='r0d')
        for stars in star:
            print(stars.text)


def main():
    new_item()


if __name__ == '__main__':
    main()