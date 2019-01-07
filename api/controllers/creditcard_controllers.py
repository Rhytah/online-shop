
from flask import jsonify, request
from api.models.creditcard_models import Creditcard
import datetime
import json


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
        self.creditcard_obj.search_creditcard(cardnumber,servicecode)
        self.creditcard_obj.addcreditcarddata()
        return jsonify ({
            "status":201,
    
            "message":"Successfully added creditcard data"
        })

    def fetch_all_creditcards(self):
        self.creditcard_obj.get_cards()
        return jsonify({
                "status":200,
                "message": "creditcards created yet"
            }),200


    def fetch_specific_card(self,cardnumber):
        result = self.creditcard_obj.get_creditcarddata(cardnumber)
        if not result:
            return jsonify({
                    "status":400,
                    "message":"Out of range  id,Try again with a valid id"
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