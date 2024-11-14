import os
import logging
from flask import Flask, render_template, request, redirect, url_for, session
import pickle
from pymongo import MongoClient
from datetime import datetime

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")

if MONGO_URI:
    try:
        # Establish connection to MongoDB
        client = MongoClient(MONGO_URI)
        print("MongoDB connection successful.")

        # Access the database
        db = client.get_database()
        print(f"Connected to database: {db.name}")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("MongoDB URI is not set in the environment variables.")
logs_collection = db.logs
user_data_collection = db.user_data

app = Flask(__name__)


# Set up logging
# Use the '/app/logs' directory which will be linked to the volume inside the container
log_file = os.path.join('/logs', 'app.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

# Load the trained model
model_path = 'diabetes_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    # Fetch the prediction from the URL query parameters if available
    prediction = request.args.get('prediction', None)
    return render_template('index.html', prediction=prediction)

@app.after_request
def add_header(response):
    # Prevent caching of the response
    response.cache_control.no_store = True
    return response

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    
    Pregnancies= float(request.form['pregnancies'])
    Glucose= float(request.form['glucose'])
    BloodPressure = float(request.form['blood_pressure'])
    SkinThickness = float(request.form['skin_thickness'])
    Insulin = float(request.form['insulin'])
    BMI = float(request.form['bmi'])
    DiabetesPedigreeFunction = float(request.form['diabetes_pedigree_function'])
    Age = float(request.form['age'])








    input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
    
    # Predict diabetes risk
    prediction = model.predict(input_data)[0]
    result = "High Risk" if prediction == 1 else "Low Risk"
    


    # Log user info and prediction result to MongoDB logs collection
    log_entry = {
        "timestamp": datetime.utcnow(),
        "name": name,
        "email": email,
        "phone": phone,
        "prediction": result
       }
    logs_collection.insert_one(log_entry)
    logging.info(f"User Data Logged: {log_entry}")

    # Save user data to MongoDB user_data collection
    user_data_entry = {
        "name": name,
        "email": email,
        "phone": phone,
        "result": result,
        "timestamp": datetime.utcnow()
    }
    user_data_collection.insert_one(user_data_entry)

    return redirect(url_for('home', prediction=result))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


