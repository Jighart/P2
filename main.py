import requests
import csv
from bs4 import BeautifulSoup
from word2number import w2n

def scrap_book(book_url):
    page = requests.get(book_url)
    soup = BeautifulSoup(page.content.decode('utf8').encode('utf8', 'ignore'), 'html.parser')

    title = soup.h1.string
    upc = soup.find_all("td")[0].string
    price_inc_tax = soup.find_all("td")[3].string.replace('£', '')
    price_exc_tax = soup.find_all("td")[2].string.replace('£', '')
    number_available = int(''.join(filter(str.isdigit, soup.find_all("td")[5].string)))
    description = soup.find("article", class_="product_page").find_all("p")[3]
    if description: description = description.string
    category = soup.find("ul", class_="breadcrumb").find_all("a")[2].string
    review = w2n.word_to_num(soup.find("p", class_="star-rating")['class'][1])
    image = soup.img['src'].replace("../..", "https://books.toscrape.com")

    headers = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

    with open('data.csv', 'a', encoding='utf8', errors='replace') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        # writer.writerow(headers)
        line = [url, upc, title, price_inc_tax, price_exc_tax, number_available, description, category, review, image]
        writer.writerow(line)

    print(title)

htmlResponse = requests.get('http://books.toscrape.com/index.html')
soup = BeautifulSoup(htmlResponse.content, 'html.parser')

categories = {}
for a in soup.find('div', {'class': 'side_categories'}).ul.find_all('a'):
    if 'books_1' not in a.get('href'):
        categories[a.text.replace('\n', '').replace('  ', '')] = 'http://books.toscrape.com/' + a.get('href')

for categorie, catUrl in categories.items():
    htmlResponse = requests.get(catUrl)
    soup = BeautifulSoup(htmlResponse.content, 'html.parser')

    if soup.find('ul', {'class': 'pager'}):
        nbPages = int(soup.find('li', {'class': 'current'}).text.split(' ')[31].replace('\n', ''))
        print(nbPages)
    else:
        nbPages = 1

    i = 0
    booksUrl = []
    while i < nbPages:
        for book in soup.find_all('article'):
            bookUrl = book.h3.a.get('href').replace('../../../', 'http://books.toscrape.com/catalogue/')
            booksUrl.append(bookUrl)
        i += 1
        if nbPages > 1:
            nextPage = requests.get(catUrl.replace('index.html', 'page-' + str(i+1) + '.html'))
            soup = BeautifulSoup(nextPage.content, 'html.parser')

    allBooksFromCurrentCategory = []
    for url in booksUrl:
        currentBook = scrap_book(url)
        allBooksFromCurrentCategory.append(currentBook)

