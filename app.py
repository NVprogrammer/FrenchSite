from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import backend
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///dict.db'
db=SQLAlchemy(app)

class Texts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    audio=db.Column(db.BLOB)
    text=db.Column(db.Text)
    def __repr__(self):
        return "<Texts %r>" % self.id

@app.route('/')
def index():
    return render_template('index.html')


correct=0
truth_word_1=''
truth_word_2=''
@app.route('/wordgame', methods = ['GET', 'POST', 'DELETE'])
def word_game():
    global correct,truth_word_1,truth_word_2
    pron=''
    if request.method == 'POST':
        form_name = request.form['form_name']
        print('form',form_name)
        if form_name == 'speak':
            pron=backend.speech_rec()
            print('pronon',truth_word_1,pron)
            if (pron == truth_word_1):
                correct += 1
            print('correct', correct)
        if form_name=='answer':
            if(pron==truth_word_1):
                correct+=1
            print('correct',correct)
    word_1, word_2 = backend.word_get_pair()
    truth_word_1, truth_word_2=word_1,word_2
    print(word_1)
    return  render_template('wordgame.html',word=word_1,inp=pron)

if __name__=='__main__':
    app.run(debug=True)