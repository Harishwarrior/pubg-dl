import requests
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)

def getlinks(image, url,btclass,apk):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', {'class': btclass})['href'] 
    print(link)
    return "<body style='display:flex;background-image:url("+image+");background-repeat: no-repeat;background-attachment: fixed;background-size: cover;background-position:center;'><a style='padding:1rem;background:linear-gradient(65deg,#F4D03F,#FCF3CF);text-decoration:none;color:black;border-radius:0.3rem;box-shadow:0px 0px 10px 2px black;font-size:large;margin:auto;align-self:center;text-shadow:2px 2px 5px black;' href='"+link+"'>++</a>"+apk+"</body>"

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/pubgm')
def pubgm():
    return getlinks("https://wallpapercave.com/wp/wp4907009.jpg","https://www.pubgmobile.com/en-US/home.shtml",'apk-btn',"PUBG MOBILE")

@app.route('/pubglite')
def pubglite():
    return getlinks('https://wallpapercave.com/wp/wp6075241.jpg','https://www.pubgmlite.com/en-US/','text-hide spr dl-apk',"PUBG LITE")

if __name__ == '__main__':
    app.run()

