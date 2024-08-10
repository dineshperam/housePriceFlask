from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

with open('House_Price.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    Rooms = int(request.form['bedrooms'])
    Bathrooms= int(request.form['bathrooms'])
    Place = int(request.form['location'])
    Area = int(request.form['area'])
    Status = int(request.form['status'])
    Facing = int(request.form['facing'])
    P_Type = int(request.form['type'])
    
    input_data = np.array([[Place,Area,Status,Rooms,Bathrooms,Facing,P_Type]])
    
    prediction = model.predict(input_data)[0]
    prediction = round(prediction)
    return render_template('home.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
