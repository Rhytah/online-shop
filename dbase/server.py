import psycopg2 
import datetime


class DatabaseConnect:
    def __init__(self):
        self.credentials = dict(
                dbname ='d4l82hlu9p9hci',
                user = 'ptyunnnqwfcjzy',
                password='bcc93c197c3ab85bcb3643bb85ae8bcb1fc2ec19c1aab7090e5180a38f285060',
                host='ec2-174-129-18-247.compute-1.amazonaws.com',
                port = 5432
              )
        
        cmd = """CREATE TABLE IF NOT EXISTS Creditcards(
            id SERIAL PRIMARY KEY,
            cardnumber INT,
            issuedate TIMESTAMP, 
            expirydate INT, 
            servicecode INT, 
            issuingbank VARCHAR (160),
            issuingagency VARCHAR(160))"""