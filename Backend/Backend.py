from flask import Flask
import os
from supabase import create_client

url = "https://dwndxnmogaexlvauvqll.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR3bmR4bm1vZ2FleGx2YXV2cWxsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzczMTI2MTYsImV4cCI6MTk5Mjg4ODYxNn0.mm097LJuyJhwGHv1bdvMskjikVYzUcqN7Rxy7N8PW_I"
supabase = create_client(url, key)

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/getAccounts', methods=['GET'])
def getAccounts():
    return list(supabase.table('Accounts').select("*").execute())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)