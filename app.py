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
    return "<body style='display:flex;'><a style='padding:1rem;background:#BDC3C7;text-decoration:none;color:#1C2833;border-radius:0.3rem;font-size:large;margin:auto;align-self:center;' href='"+link+"'>PUBG Mobile</a></body>"
    
@app.route('/pubglite')
def getlinklite():
    URL = 'https://www.pubgmlite.com/en-US/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', {'class': 'text-hide spr dl-apk'})['href'] 
    print(link)
    return "<body style='display:flex;'><a style='padding:1rem;background:#BDC3C7;text-decoration:none;color:#1C2833;border-radius:0.3rem;font-size:large;margin:auto;align-self:center;' href='"+link+"'>PUBG lite</a></body>"


if __name__ == '__main__':
    app.run()
