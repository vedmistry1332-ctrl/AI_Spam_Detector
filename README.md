# AI Spam Message Detector

An AI-based Spam Message Detector that uses Machine Learning to classify SMS messages as either **SPAM** or **NOT SPAM**.

This project was developed as a college project to understand how Natural Language Processing (NLP) and Machine Learning can be used for text classification.

---

## Project Overview

Spam messages are unwanted messages that may contain advertisements, fake offers, suspicious links, or other unwanted content.

This project takes an SMS message as input and predicts whether the message is:

- SPAM
- NOT SPAM

The application provides a simple web interface using Streamlit.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Streamlit
- Joblib

---

## Machine Learning Process

The project follows these steps:

```text
SMS Dataset
     ↓
Data Loading
     ↓
Train-Test Split
     ↓
TF-IDF Vectorization
     ↓
Multinomial Naive Bayes
     ↓
Model Training
     ↓
Prediction
     ↓
SPAM / NOT SPAM
Dataset

The project uses the SMS Spam Collection dataset.

The dataset contains SMS messages classified into two categories:

ham - legitimate message
spam - spam message

The dataset contains 5,574 SMS messages.

Project Structure
AI_Spam_Detector/
│
├── dataset/
│   ├── SMSSpamCollection
│   └── spam.csv
│
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── app.py
├── convert_dataset.py
├── train_model.py
├── requirements.txt
└── README.md
File Description
File / Folder	Purpose
dataset/	Contains the SMS dataset
SMSSpamCollection	Original SMS Spam Collection dataset
spam.csv	Converted CSV version of the dataset
model/	Contains the trained model files
spam_model.pkl	Saved Naive Bayes model
vectorizer.pkl	Saved TF-IDF vectorizer
convert_dataset.py	Converts the original dataset into CSV format
train_model.py	Trains and saves the machine learning model
app.py	Streamlit web application
requirements.txt	Python libraries required for the project
README.md	Project documentation
How the Model Works
1. Data Loading

The SMS dataset is loaded using Pandas.

2. Train-Test Split

The dataset is divided into:

80% training data
20% testing data
3. TF-IDF

SMS messages are text data, so they need to be converted into numerical values before they can be given to a machine learning algorithm.

TF-IDF (Term Frequency-Inverse Document Frequency) converts the text into numerical features.

4. Multinomial Naive Bayes

The project uses the Multinomial Naive Bayes algorithm for classification.

The trained model learns patterns from spam and legitimate messages.

5. Prediction

When a user enters a new SMS message, the message is converted using the trained TF-IDF vectorizer and passed to the trained model.

The model then predicts:

SPAM

or

NOT SPAM
Installation
Step 1: Clone the Repository
git clone https://github.com/your-username/AI_Spam_Detector.git

Move into the project folder:

cd AI_Spam_Detector
Step 2: Install Required Libraries

Run:

python -m pip install -r requirements.txt
Running the Project

Run the Streamlit application:

python -m streamlit run app.py

After running the command, Streamlit will provide a local URL.

Open the URL in your browser.

Example

Enter a message such as:

Congratulations! You have won a free prize. Click the link to claim now.

The application may classify it as:

SPAM

For a normal message such as:

Hey, are we meeting at 5 today?

The application may classify it as:

NOT SPAM
Model Training

If you want to train the model again, run:

python train_model.py

This will create/update:

model/spam_model.pkl
model/vectorizer.pkl
Dataset Conversion

If the original SMSSpamCollection dataset is being used, run:

python convert_dataset.py

This creates:

dataset/spam.csv
Requirements

The main Python libraries used in this project are:

pandas
scikit-learn
streamlit
joblib
Future Improvements

Some possible improvements for the project are:

Improve the accuracy of the model
Add more machine learning algorithms
Display prediction probability
Add message history
Improve the user interface
Deploy the application online
Add support for multiple languages
Project Purpose

This project was created for educational purposes to understand:

Machine Learning
Natural Language Processing
Text Classification
TF-IDF
Naive Bayes
Streamlit
Building a complete ML application
Author

Your Name

College Project - AI Spam Message Detector


### One important thing before uploading to GitHub

Since your project contains trained model files:

```text
model/spam_model.pkl
model/vectorizer.pkl

you can upload them to GitHub for this college project so that someone cloning your repository can run app.py without retraining.

Also make sure your requirements.txt contains:

pandas
scikit-learn
streamlit
joblib

Then your GitHub repository will have a clean structure:

AI_Spam_Detector
│
├── dataset
├── model
├── app.py
├── convert_dataset.py
├── train_model.py
├── requirements.txt
└── README.md
