# Project: Flask Web Application for House Price Prediction Using a Machine Learning Model

## Introduction:

In this project, I developed the predictive power of a model trained on houses price data. It deploys with flask API and using Linear Regression to predict the price value. Deploy Machine Learning Model Using Flask to take a model from python code.<br>

### It contains the following parts:

1. Setup your environment<br>
2. Build your house price prediction model<br>
3. Create flask API<br>

## Setup your environment

To run the web app on your local computer, install the required libraries, These packages are <br>

1. python 3.8.0
2. flask 2.0.1
3. werkzeug 2.0.1
4. sci-kit learn
5. pandas
6. numpy
7. pickle

## Build your house price prediction model

### Step 1: Understand the data

The first step of model prediction is to understand the data. It is more important to all machine learning and deep learning projects. You can find more information about the data, go to House Price - Advanced Regression Techniques competition in Kaggle (Note: If you don't know Kaggle, please check this blog What is Kaggle? How to use it?). And it is also available in my repositories and find the dataset or click this link: dataset.<br>

### Step 2: Import the Packages

Create a python file (for example house.py). After installed the required packages, import packages  in your python file.<br>
<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.1.png'></img>
<br>
<br>

### Step 3: Import the data

Next, import the data using pandas<br>
<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.2.png'></img>
<br>
<br>

### Step 4: Feature Selection 

Remove the unwanted features (Columns), now choose columns are  number of bedrooms, number of bathrooms, number of floors, year of build, and price of the house. In price of the house is the target value. We trained the model in the other four columns to find the price of the house.<br>
<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.3.png'></img>
<br>
<br>

### Step 5: Split the data
    
We want to create a model, must have split it into training and testing. the model trained by training dataset and then apply the evaluation of model used by test dataset.<br>

<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.4.png'></img>
<br>
<br>

### Step 6: Create Machine Learning Model
    
Now, we use Linear regression model to predict the house price.<br>

<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/1.5.png'></img>
<br>
<br>

### Step 7: Dump the model using pickle

It used to store the model data in a file<br>

<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.6.png'></img>
<br>
<br>

## Create Flask API

Flask is a web framework for python. It is used for managing HTTP request and render templates. Now, start to create basic flask API (for example app.py).<br> 

Pickle load function is used to load the model data in flask API. App route('/') map to home page('index.html') and App route(/predict) map to predict function, it is also call in home page. In predict function get the values from the form and then used them for model prediction.<br>

<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.7.png'></img>
<br>
<br>

Finally, create simple form in html<br>
<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.8.png'></img>
<br>
<br>

## Preview:
1. Submission form:
<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.9.png'></img>
<br>
<br>

2. Result in IDE VS code:

<img src='https://github.com/dineshperam/housePriceFlask/blob/main/projimages/img%201.91.png'></img>
<br>
<br>


## Download this as Zip file or use git clone url

1. After Downloading/cloning the project install the necessary requirements.txt, use the command:<br><br>
```
pip install requirements.txt
```
<br>
<br>

## Conclusion:

To run code on your computer, following command in terminal<br>
```
python house-price.py
```
<br>

After running the python file,<br>

Project Runs on http://127.0.0.1:5000 <br>

In summary, we created the House Price Prediction using Linear Regression and deploy with Flask application of the given  dataset.<br>

## License
MIT License
<br>
<br>

### Thank you
