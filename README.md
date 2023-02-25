# ByteMe
iNTUition v9.0 Repo

# Backend Setup
1) Create a virtual env in python in the project backend directory ```py -m pip install --user virtualenv```   
2) Activate the virtual env ```.\env\Scripts\activate```   
3) Change directory ```cd Backend```    
4) Install all requiered libraries ```pip install -r requirements.txt```    
5) To run type ```python Backend.py```
6) Keep checking a regular intervals and updating requierments.txt using ```pip freeze```    

# Backend API Docs
##### All to be passed in form-data in Postman

## POST localhost:9000/oneLineSummary/
paper (pdf file)

## POST localhost:9000/getWordCloud/
paper (pdf file)

## GET localhost:9000/searchPapers/
keyword (word from search)
