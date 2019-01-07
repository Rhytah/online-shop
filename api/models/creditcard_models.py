import datetime
from dbase.server import DatabaseConnect
from flask import jsonify

db=DatabaseConnect()
class Creditcard:
    
    def get_cards(self):
        cmd = "SELECT * FROM Creditcards;"
        db.cursor.execute(cmd)
        all_cards = db.cursor.fetchall()
        return all_cards


    def addcreditcarddata(self):
      add_creditcard = " INSERT INTO Creditcards(id,cardnumber,issuedate, expirydate, servicecode, issuingbank,issuingagency);"
      db.cursor.execute(add_creditcard)

        

    def get_creditcarddata(self,cardnumber):
        cmd= "SELECT * FROM Creditcards WHERE cardnumber='{}'".format(cardnumber)
        db.cursor.execute(cmd)
        result=db.cursor.fetchone()
        if result:
            return result
        else:
            return {"message":"Card doesn't exist"}

    def search_creditcard(self,cardnumber,servicecode):
        cmd= "SELECT * FROM Creditcards WHERE cardnumber='{}',servicecode='{}'".format(cardnumber,servicecode)
        db.cursor.execute(cmd)
        result=db.cursor.fetchone()
        if result:
            return jsonify({"status":400,
            "data": (cardnumber,servicecode),
            "message":"Card already exists"})

    def deletecard(self,cardnumber):
        cmd= "DELETE FROM Creditcards WHERE cardnumber='{}".format(cardnumber)
        result= db.cursor.rowcount
        db.cursor.execue(cmd)
        