from api import app
from flask import Flask
from dbase.server import DatabaseConnect
db=DatabaseConnect()  

if __name__=='__main__':
    app.run(debug=True, port=5000)
    db=DatabaseConnect()