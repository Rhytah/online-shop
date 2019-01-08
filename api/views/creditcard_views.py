from flask import Flask, json, jsonify, request,Blueprint, current_app as app
from api.controllers.creditcard_controllers import CardController


cue=CardController()
@app.route('/')
@app.route('/index')
def index():
    return "Welcome to online shop"
    

@app.route('/creditcard', methods = ['POST'])
def add_creditcarddata():
    return cue.add_card
@app.route('/creditcard')
def get_creditcards():
    return cue.fetch_all_creditcards

@app.route('/creditcard/int:cardnumber')
def fetchsinglecarddata():
    return cue.fetch_specific_card

@app.route('/creditcard/int:cardnumber', methods = ['PUT'])
def update_creditcarddata():
    return cue.update_card

@app.route('/creditcard/int:cardnumber', methods = ['DELETE'])
def deletecard():
    return cue.delete_card



