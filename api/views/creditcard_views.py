from flask import Flask, json, jsonify, request,Blueprint, current_app as app
from api.controllers.creditcard_controllers import CardController


cue=CardController()
@app.route('/')
@app.route('/index')
def index():
    return "Welcome to online shop"

@app.route('/creditcard', methods = ['POST'])
def add_creditcarddata():
    pass
