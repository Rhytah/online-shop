
from flask import Flask, jsonify, request,json
from api.models.creditcard_models import Creditcard
import datetime



class CardController:
    def __init__(self):
        self.creditcard_obj = Creditcard()
    def add_card(self):
        data = request.get_json()
        cardnumber = data.get('cardnumber')
        expirydate = data.get('expirydate')
        servicecode = data.get('servicecode')
        issuingbank = data.get('issuingbank')
        issuingagency = data.get('issuingagency')        
        invalidentry=self.creditcard_obj.search_creditcard(cardnumber)
        if invalidentry:
            return "Creditcard data already exists"
        self.creditcard_obj.addcreditcarddata(cardnumber,expirydate,servicecode,issuingbank,issuingagency)
        return jsonify ({
            "status":201,
    
            "message":"Successfully added creditcard data"
        })

    def fetch_all_creditcards(self):
        result=self.creditcard_obj.get_cards()
        if result:
            return jsonify({
                    "status":200,
                    "message": "creditcards created so far",
                    "data":result
                }),200    
        return jsonify({
                "status":200,
                "message": "No creditcards created yet"
            })


    def fetch_specific_card(self,cardnumber):
        result = self.creditcard_obj.get_creditcarddata(cardnumber)
        if not result:
            return jsonify({
                    "status":400,
                    "message":"Card doesnot exist.Out of range  id,Try again with a valid id"
                }),200
        return jsonify({
                    "status":200,
                    "data":result,
                    "message":"This is the creditcard data"
                }),200


    def delete_card(self,cardnumber):
        deleteresult=self.creditcard_obj.deletecard(cardnumber)
        if deleteresult:
            return jsonify({
                "status":200,
                "message":"Creditcarddata has been deleted"
            })
        return jsonify({
                "status":400,
                "message":"Invalid cardnumber"
            })
    
    def update_card(self,cardnumber):
        return jsonify({
            "status":200,
            "message":"you this shows updated data"
        })