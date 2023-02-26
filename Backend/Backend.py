import asyncio
from flask import Flask, request
from flask_cors import CORS
import os
from pathlib import Path
import shutil
from werkzeug.utils import secure_filename
from makeGraph import make_wordcloud
from RunML import oneLineSummary, getCategoryWeights, getNouns
from pdfExtract import extract_text_from_pdf
from supabase import create_client
import json

url = "https://dwndxnmogaexlvauvqll.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR3bmR4bm1vZ2FleGx2YXV2cWxsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzczMTI2MTYsImV4cCI6MTk5Mjg4ODYxNn0.mm097LJuyJhwGHv1bdvMskjikVYzUcqN7Rxy7N8PW_I"
supabase = create_client(url, key)
func = supabase.functions()

app = Flask(__name__)
'''try:
    path = os.path.dirname(os.path.abspath(__file__))
    upload_folder=os.path.join(path.replace("/file_folder",""),"tmp")
    os.makedirs(upload_folder, exist_ok=True)
    app.config['upload_folder'] = upload_folder
except Exception as e:
    app.logger.info("An error occurred while creating temp folder")
    app.logger.error("Exception occurred : {}".format(e))'''
CORS(app, origins='*')

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/getAccounts/', methods=['GET'])
def getAccounts():
    return list(supabase.table('Accounts').select("*").execute())

@app.route('/searchPapers/', methods=['POST'])
def searchPapers():
    # Getting data
    keyword = request.form['keyword']
    new_keyword = "% " + keyword + " %"
    return_stuff = supabase.table('Papers').select("title, link").like('description',new_keyword).execute()
    print("resturn stuff = ", return_stuff.data)
    return return_stuff.data

@app.route('/oneLineSummary/', methods=['POST'])
def OneLineSummary():
    # Saving the file
    f = request.files['paper']
    new_file_path = "Files_Sent/" + secure_filename(f.filename)
    f.save(new_file_path)
    # Extracting abstract from pdf
    abstract = extract_text_from_pdf(new_file_path)
    one_line_summary = oneLineSummary(abstract)
    return one_line_summary

@app.route('/getWordCloud/', methods=['POST'])
def getWordCloud():
    # Saving the file
    f = request.files['paper']
    new_file_path = "Files_Sent/" + secure_filename(f.filename)
    f.save(new_file_path)
    # Extracting abstract from pdf
    abstract = extract_text_from_pdf(new_file_path)
    noun_list = getNouns(abstract)
    words, weights = getCategoryWeights(abstract=abstract, categories=noun_list)
    img_encoding = make_wordcloud(words, weights)
    return img_encoding

'''@app.route('/searchPapers/', methods=['GET'])
def searchPapers():
    # Getting data
    keyword = request.form['keyword']

    try:
        loop = asyncio.get_event_loop()
    except:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    resp = loop.run_until_complete(test_func(loop, keyword))
    loop.close()
    print('resp == ', resp)
    return resp

@asyncio.coroutine
async def test_func(loop, keyword):
    resp = await func.invoke("RunSearch1",invoke_options={'body':{keyword}})
    return resp'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)