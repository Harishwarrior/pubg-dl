import requests
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/pubgm')
def getlinks():
    URL = 'https://www.pubgmobile.com/en-US/home.shtml'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', {'class': 'apk-btn'})['href'] 
    print(link)
    return "<a class='padding:0.5rem;background:gray;text-decoration:none;color:black;' href='"+link+"'>PUBG Mobile</a>"
    
@app.route('/pubglite')
def getlinklite():
    URL = 'https://www.pubgmlite.com/en-US/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', {'class': 'text-hide spr dl-apk'})['href'] 
    print(link)
    return "<a class='padding:0.5rem;background:gray;text-decoration:none;color:black;' href='"+link+"'>PUBG lite</a>"


if __name__ == '__main__':
    app.run()
