from flask_sqlalchemy import SQLAlchemy
from app import app
from selenium import webdriver
from bs4 import BeautifulSoup
db=SQLAlchemy(app)

class Texts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    audio=db.Column(db.BLOB)
    text=db.Column(db.Text)
    def __repr__(self):
        return "<Texts %r>" % self.id

def add_text(audio,text):
    Text=Texts(audio=audio,text=text)
    try:
        db.session.add(Text)
        db.session.commit()
    except:
        pass

def get_text(url,driver):
    for i in url:
        driver.get(i)

driver = webdriver.Firefox()
driver.get('https://reallanguage.club/francuzskie-teksty-nachalnogo-urovnya-s-audio/')


html = driver.page_source
soup = BeautifulSoup(html)


