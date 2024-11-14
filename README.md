

# Diabetic Risk Prediction App

## Overview

Welcome to the **Diabetic Risk Prediction App**! This web application leverages machine learning to predict the likelihood of a person being at risk for diabetes based on various medical features such as glucose level, BMI, age, and more. The app is built using the Flask web framework and is containerized with Docker for easy deployment. It connects to a MongoDB database for logging user data and storing prediction results. The app is deployed on **Render**, a cloud platform, with continuous integration via GitHub.

## Key Features

- **Diabetes Risk Prediction:** Users provide medical information, and the app predicts whether they are at high or low risk of developing diabetes.
- **Machine Learning Model:** The app uses a Random Forest Classifier to analyze input data and generate predictions.
- **Data Logging:** User details and prediction outcomes are logged in a MongoDB database for tracking and analysis.
- **Containerized App:** The app is packaged in a Docker container, ensuring portability and easy deployment.
- **Cloud Deployment:** The app is deployed on Render, a platform that enables hassle-free hosting of web applications.

## Technologies Used

- **Backend:** Flask (Python)
- **Machine Learning:** Random Forest Classifier (scikit-learn)
- **Database:** MongoDB (Cloud connection via MongoDB URI)
- **Containerization:** Docker
- **Deployment:** Render (cloud platform)
- **Environment Management:** Environment variables managed via `.env` file

## How to Use

1. **Clone the Repository:**  
   Start by cloning this repository to your local machine to work with the app’s codebase.

2. **Set Up Dependencies:**  
   The app relies on several Python packages. Install these packages by using the `requirements.txt` file.

3. **MongoDB Connection:**  
   To connect the app to MongoDB, you will need to set up a MongoDB instance. We recommend using **MongoDB Atlas** for a cloud-based solution. You will need to provide the connection string (URI) to the app through an environment variable.

4. **Run the App Locally:**  
   The app can be run locally after setting up the environment and dependencies. Once started, the app will be available in your web browser where you can input data and view the diabetes risk prediction.

5. **Dockerization (Optional):**  
   If you prefer, you can build and run the app inside a Docker container. This ensures that the app runs consistently across different environments.

6. **Deployment on Render:**  
   Once you're ready to deploy, you can push your code to GitHub and link your repository to Render. Render will automatically build and deploy the application, making it accessible to users worldwide.

## Deployment Steps

1. **GitHub Integration:**  
   Push your code to GitHub if you haven't already. Ensure that all necessary files, including the `Dockerfile` and `.env` file, are in the repository.

2. **Render Setup:**  
   Sign up for an account on [Render](https://render.com) and create a new web service. Connect your GitHub repository to Render, and it will automatically pull the latest commit and deploy the app.

3. **Set Environment Variables on Render:**  
   On Render, navigate to the settings for your app and add the necessary environment variables, such as the `MONGO_URI`, to connect to your MongoDB database.

4. **Automatic Deployment:**  
   Render will build your app, run the necessary containers, and deploy it to the web. Once deployed, Render will provide a URL where the app can be accessed.


## Future Enhancements

- **Improved User Interface:** Enhance the web interface to make it more user-friendly.
- **Expanded Model:** Explore additional machine learning models for improved prediction accuracy.


## Contributing

We welcome contributions to improve this project. If you have any suggestions, bug fixes, or new features, feel free to fork the repository and submit a pull request.

## Links

This project is published on https://diabetrack.onrender.com/

---

This README provides a clear and organized description of your app, its features, and how to set it up, run it, and deploy it. It’s formatted for easy copy-pasting into your GitHub repository.
