from bs4 import BeautifulSoup
import requests


header = {
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X; sl-SI) AppleWebKit/531.3.1 (KHTML, like Gecko) Version/4.0.5 Mobile/8B111 Safari/6531.3.1'
}


def categories_electronics():
    url = 'https://www.wildberries.ru/catalog/elektronika'
    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')

    sub_content = soup.find_all('a', class_='j-menu-item')
    for i in sub_content:
        a = i.find('href')
        print(a)


def main():
    categories_electronics()


if __name__ == '__main__':
    main()