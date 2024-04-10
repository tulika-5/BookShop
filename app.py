from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('decision_tree_model.pkl')

# Define route for index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

# Define route for base page
@app.route('/base')
def base():
    return render_template('base.html')
@app.route('/login_register')
def login_register():
    return render_template('LoginRegister.html')


# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        price = float(request.form['price'])
        year_old = float(request.form['year_old'])
        availability = float(request.form['availability'])
        stars = float(request.form['stars'])
        
        # Standardize the input
        scaler = StandardScaler()
        input_data = scaler.fit_transform([[price, year_old, availability, stars]])
        
        # Make prediction
        predicted_price = model.predict(input_data)[0]
        
        return jsonify({'predicted_price': predicted_price}) # Return prediction as JSON response

if __name__ == '__main__':
    app.run(debug=True)
