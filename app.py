
# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import appmodel # load appmodel.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
     
    #take data from form and store in each feature    
    
    input_features = [x for x in request.form.values()]

    location = input_features[0]
    area = input_features[1]
    furnishing = input_features[2]
    facing = input_features[3]
    balcony = input_features[4]
    bathroom = input_features[5]
    power = input_features[6]
    bedroom = input_features[7]
    flooring = input_features[8]
    parking = input_features[9]
    age = input_features[10]
    transit = input_features[11]
    
     
    # predict the price of house by calling model.py
    predicted_price = appmodel.predict_price(flooring, facing, location, area, bedroom, bathroom, balcony, parking, power, age, furnishing, transit)       
 
 
    # render the html page and show the output
    return render_template('result.html', prediction_text='Predicted Valuation of House is Rs. {} /-'.format(predicted_price))
    
if __name__ == '__main__':
	app.run(debug=True)
