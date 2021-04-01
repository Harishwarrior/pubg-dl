import requests
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/pubgm')
def getlinks():
    img='https://wallpapercave.com/wp/wp4907009.jpg'
    URL = 'https://www.pubgmobile.com/en-US/home.shtml'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', {'class': 'apk-btn'})['href'] 
    print(link)
    return "<body style='display:flex;background-image:url("+img+");background-repeat: no-repeat;background-attachment: fixed;background-size: cover;background-position:center;'><a style='padding:1rem;background:linear-gradient(65deg,#F4D03F,#FCF3CF);text-decoration:none;color:black;border-radius:0.3rem;box-shadow:0px 0px 10px 2px black;font-size:large;margin:auto;align-self:center;text-shadow:2px 2px 5px black;' href='"+link+"'>PUBG Mobile</a></body>"
    
@app.route('/pubglite')
def getlinklite():
    img='https://wallpapercave.com/wp/wp6075241.jpg'
    URL = 'https://www.pubgmlite.com/en-US/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', {'class': 'text-hide spr dl-apk'})['href'] 
    print(link)
    return "<body style='display:flex;background-image:url("+img+");background-repeat: no-repeat;background-attachment: fixed;background-size: cover;background-position:center;'><a style='padding:1rem;background:linear-gradient(65deg,#F4D03F,#FCF3CF);text-decoration:none;color:black;border-radius:0.3rem;box-shadow:0px 0px 10px 2px black;font-size:large;margin:auto;align-self:center;text-shadow:2px 2px 5px black;' href='"+link+"'>PUBG lite</a></body>"


if __name__ == '__main__':
    app.run()
