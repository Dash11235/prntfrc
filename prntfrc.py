import requests
import random
import re
from bs4 import BeautifulSoup

def main():
    #for i in range(10):
    #    print(generatePage())

    page = generate_page()
    url = "https://prnt.sc/"+page
    response = requests.get(url, headers={'User-Agent': 'Chrome'})
    html = BeautifulSoup(response.text, 'html.parser')
    img = html.find_all('img', class_="no-click screenshot-image")

    img = str(img[0])

    try:
        img_url = re.search('src="(.+?)"', img).group(1)
    except AttributeError:
        img_url = ''

    print(img_url)

    #print(page)
    #print(img)


def generate_page():
    st = ""
    nd = ""

    for i in range(2):
        st = st+chr(random.randint(97,122))

    for i in range(4):
        nd = nd+str(random.randint(0,9))

    return st+nd

main()


