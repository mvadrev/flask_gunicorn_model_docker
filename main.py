from flask import Flask, redirect, url_for, request
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("sentiment-analysis")



@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      return classifier(request.form['input'])
   if request.method == 'GET':
    return 'Please post a string to localhost:5000 with input as the string and application json headers - Eg use postman, Insomnia'



if __name__ == '__main__':
   app.run()


