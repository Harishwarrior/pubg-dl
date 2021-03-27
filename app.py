import requests
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api')
def getlinks():
    URL = 'https://www.pubgmobile.com/en-US/home.shtml'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', {'class': 'apk-btn'})['href'] 
    print(link)
    return link
    

if __name__ == '__main__':
    app.run()