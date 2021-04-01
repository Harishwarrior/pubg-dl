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
    return "<body style='display:flex;background-image:url('https://wallpapercave.com/wp/wp4907009.jpg');background-repeat: no-repeat;background-attachment: fixed;background-size: cover;'><a style='padding:1rem;background:#BDC3C7;text-decoration:none;color:#1C2833;border-radius:0.3rem;box-shadow:0px 0px 10px 0px #BDC3C7;font-size:large;margin:auto;align-self:center;' href='"+link+"'>PUBG Mobile</a></body>"
    
@app.route('/pubglite')
def getlinklite():
    URL = 'https://www.pubgmlite.com/en-US/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', {'class': 'text-hide spr dl-apk'})['href'] 
    print(link)
    return "<body style='display:flex;background-image:url('https://wallpapercave.com/wp/wp4211445.jpg');background-repeat: no-repeat;background-attachment: fixed;background-size: cover;'><a style='padding:1rem;background:#BDC3C7;text-decoration:none;color:#1C2833;border-radius:0.3rem;box-shadow:0px 0px 10px 0px #BDC3C7;font-size:large;margin:auto;align-self:center;' href='"+link+"'>PUBG lite</a></body>"


if __name__ == '__main__':
    app.run()
