# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:44:39 2020

@author: Rohit Mehta
"""

from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle


model = pickle.load(open('spam_detector.pkl','rb'))
cv = pickle.load(open('transform.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = model.predict(vect)
	return render_template('result.html',prediction = my_prediction)    


if __name__ == '__main__':
	app.run(debug=True)    