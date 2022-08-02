import requests
import csv
from bs4 import BeautifulSoup
from word2number import w2n

url = "https://books.toscrape.com/catalogue/forever-rockers-the-rocker-12_19/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.h1.string
upc = soup.find_all("td")[0].string
price_inc_tax = soup.find_all("td")[3].string
price_exc_tax = soup.find_all("td")[2].string
number_available = int(''.join(filter(str.isdigit, soup.find_all("td")[5].string)))
description = soup.find("article", class_="product_page").find_all("p")[3].string
category = soup.find("ul", class_="breadcrumb").find_all("a")[2].string
review = w2n.word_to_num(soup.find("p", class_="star-rating")['class'][1])
image = soup.img['src'].replace("../..","https://books.toscrape.com")

headers = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(headers)
    line = [url, upc, title, price_inc_tax, price_exc_tax, number_available, description, category, review, image]
    writer.writerow(line)

print(review)
