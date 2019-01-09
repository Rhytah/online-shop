from flask import Flask, json, jsonify, request,Blueprint, current_app as app
from api.controllers.creditcard_controllers import CardController


cue=CardController()
@app.route('/')
@app.route('/index')
def index():
    welcomemessage ="""
    <!DOCTYPYE html>
    <html>
        <head>
        <title> Onlineshop API</title>
      
        </head>
        <body>
        <div class=maincontent>
            <h2>Onlineshop-API<h2>
            Currently supported endpoints
            <br>

            <a href='https://rhytahduka.herokuapp.com/creditcard'>Fetch all creditcard data</a>
            <br>
            <a href='https://rhytahduka.herokuapp.com/creditcard' method='POST'>Add creditcard data</a>
            <br>
            <a href='https://rhytahduka.herokuapp.com/creditcard/<int:cardnumber'>Fetch specific single creditcard data</a>
            <br>
            <a href='https://rhytahduka.herokuapp.com/creditcard/<int:cardnumber' method='PUT'>Update specific single creditcard data</a>
            <br>
            <a href='https://rhytahduka.herokuapp.com/creditcard/<int:cardnumber' method='DELETE'>delete specific single creditcard data</a>
        </div>
        </body>
        </html>
    """
    return welcomemessage
    

@app.route('/creditcard', methods = ['POST'])
def add_creditcarddata():
    return cue.add_card()
@app.route('/creditcard', methods=['GET'])
def get_creditcards():
    return cue.fetch_all_creditcards()

@app.route('/creditcard/<int:cardnumber>',methods=['GET'])
def fetchsinglecarddata(cardnumber):
    return cue.fetch_specific_card(cardnumber)

@app.route('/creditcard/<int:cardnumber>', methods = ['PUT'])
def update_creditcarddata(cardnumber):
    return cue.update_card(cardnumber)

@app.route('/creditcard/<int:cardnumber>', methods = ['DELETE'])
def deletecard(cardnumber):
    return cue.delete_card(cardnumber)



