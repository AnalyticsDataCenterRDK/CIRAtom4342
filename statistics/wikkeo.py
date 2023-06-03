from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")

options.headless = True


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


header = {
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X; sl-SI) AppleWebKit/531.3.1 (KHTML, like Gecko) Version/4.0.5 Mobile/8B111 Safari/6531.3.1'
}


def categories_electronics():
    url = 'https://wikkeo.com/category/electric'
    response = requests.get(url, headers=header, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    sub_content = soup.find_all('div', {'class': 'sub-content open level2'})
    for i in sub_content:
        a = i.find('a')
        href = a.get('href')
        print('Ссылка на категорию -',href, 'Название категории -',i.text)

        sub_categories_url = href
        sub_categories_response = requests.get(sub_categories_url, headers=header, verify=False)

        soup_sub = BeautifulSoup(sub_categories_response.text, 'html.parser')

        sub_content_categories = soup_sub.find_all('div', {'class': 'sub-content open level2'})
        for j in sub_content_categories:
            b = j.find('a')
            href_subcategories = b.get('href')
            print('Ссылка на подкатегорию -',href_subcategories, 'Название подкатегории -',j.text)

            sub_sub_url = href_subcategories
            sub_sub_categories_response = requests.get(sub_sub_url, headers=header, verify=False)

            soup_sub_sub = BeautifulSoup(sub_sub_categories_response.text, 'html.parser')

            product_name = soup_sub_sub.find_all('div', {'class': 'product-name'})
            for h in product_name:
                c = h.find('a')
                href_c = c.get('href')
                print('Ссылка на товар -', href_c, 'Название продукта -', h.text)

                url_item = href_c
                response_item = requests.get(url_item, headers=header, verify=False)

                star_soup = BeautifulSoup(response_item.text, 'html.parser')

                star = star_soup.find_all('div', {'class': 'rate'})
                for stars in star:
                    print('Кол-во звезд -',stars.text)

                    sale = star_soup.find_all('div', {'class': 'selled'})
                    for sales in sale:
                        print('Продано -',sales.text)

                        url_rewiew = url_item
                        response_url_rewiew = requests.get(url_rewiew, headers=header, verify=False)

                        rewiew_soup = BeautifulSoup(response_url_rewiew.text, 'html.parser')

                        rewiew = rewiew_soup.find_all('div', {'class': 'review-info'})
                        for rewiews in rewiew:
                            print('Отзыв пользователя',rewiews.text)


def main():
    categories_electronics()


if __name__ == '__main__':
    main()