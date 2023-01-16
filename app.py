#!/usr/bin/env python
# coding: utf-8

import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np

# create instance of Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print("I am In hello. Made some changes")
    return render_template('index.html')

@app.route('/api',methods=['POST'])
def predict():
    print("Request.method:", request.method)
    print("Request.TYPE", type(request))
    print("In the process of making a prediction.")

    if request.method == 'POST':
        print(request.form)
        age = request.form['age']
        sex = request.form['experience']
        job = request.form['income']
        housing = request.form['zipcode']
        saving_account = request.form['family']
        checking_amount = request.form['ccavg']
        credit_amount = request.form['education']
        duration = request.form['mortgage']

        test_arr = np.array([age, sex, job, housing, saving_account, checking_amount, credit_amount, duration]).reshape(1,8)

        # Read the machine learning model
        pickle_file = open('model2.pkl', 'rb')     
        model = pickle.load(pickle_file)

        # Make prediction
        prediction = model.predict(test_arr)

        # Take the first value of prediction
        output = prediction[0]

        predicted = "The customer will purchase the loan!" if int(output) == 1 else "The customer will not buy the loan!" 
        result = f"RESULT: {predicted}"
        return render_template('index.html', result=result)
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

