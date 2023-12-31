import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

s = HTMLSession()

def scrapeData(category , maxPages):

    baseUrl = "https://www.flipkart.com"
    url = f"https://www.flipkart.com/search?q={category}"
    page = 1

    data = []

    def getdata(url):
        r = s.get(url)
        soup = BeautifulSoup(r.text , 'html.parser')
        return soup

    def getNextPage():
        nonlocal page , maxPages
        if page == maxPages:
            return None
        page+=1
        return baseUrl + f'/search?q={category}&page={page}'

    def cleanPrice(price):
        result = []
        for j in price:
            if j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                result.append(j)
        result = ''.join(result)
        result = int(result)
        return result

    while True:
        if url == None:
            break

        soup = getdata(url)
        products:BeautifulSoup = soup.find_all('div' , {'class' : '_13oc-S'})

        for i in products:
            title:str = i.find('div' , {'class' : '_4rR01T'}).text
            price:str = i.find('div' , {'class' : '_30jeq3 _1_WHN1'}).text

            productLink = baseUrl + i.find('a' , {'class' : '_1fQZEK'})['href']
            productSoup = getdata(productLink)

            allImages = []
            images = productSoup.find_all('li' , {'class' : '_20Gt85 _1Y_A6W'})
            for img in images:
                allImages.append(img.find('img')['src'].replace('128/128' , '416/416'))

            allHighlights = []
            highlights = i.find_all('li' , {'class' : 'rgWa7D'})
            for highlight in highlights:
                allHighlights.append(highlight.text)

            description = "_HSR_".join(allHighlights)

            data.append({
                'title' : title,
                'price' : cleanPrice(price),
                'description' : description,
                'images' : allImages
            })
            
        url = getNextPage()

    return data