# import necessary libraries
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np
import pandas as pd

model_run = pickle.load(open('model.pickle','rb'))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://aapszkgtddwxos:7902cbf4ca9a3751f840fc7caac5e6678f79f9d7466d670a9d735875702031f5@ec2-3-211-149-196.compute-1.amazonaws.com:5432/dau19t0359mkr0'

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Remove auto sort
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

class Request(db.Model):
    __tablename__ = 'location_info'
    id = db.Column(db.Integer, primary_key=True)
    High_School = db.Column(db.Float)
    Bachelors = db.Column(db.Float)
    Never_Married = db.Column(db.Float)
    Married = db.Column(db.Float)
    Male = db.Column(db.Float)
    Black = db.Column(db.Float)
    Hispanic_Latino = db.Column(db.Float)
    White = db.Column(db.Float)
    Unemployment = db.Column(db.Float)
    High = db.Column(db.Float)
    def __init__(self, High_School, Bachelors, Never_Married, Married, Male, Black, Hispanic_Latino, White, Unemployment, High):
        self.High_School = High_School
        self.Bachelors = Bachelors
        self.Never_Married = Never_Married
        self.Married = Married
        self.Male = Male
        self.Black = Black
        self.Hispanic_Latino = Hispanic_Latino
        self.White = White
        self.Unemployment = Unemployment
        self.High = High

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        High_School=request.form['high_school']
        Bachelors=request.form['bachelors']
        Never_Married = request.form['never_married']
        Married = request.form['married']
        Male = request.form['male']
        Black=request.form['black']
        Hispanic_Latino=request.form['hispanic_latino']
        White=request.form['white']
        Unemployment = request.form['unemployment']
        High = request.form['high']
        

        data = Request(High_School, Bachelors, Never_Married, Married, Male,Black, Hispanic_Latino, White, Unemployment, High)
        db.session.add(data)
        db.session.commit()
        
        final_features = np.array([[High_School, Bachelors, Never_Married, Married, Male,Black, Hispanic_Latino, White, Unemployment, High]])
        prediction = model_run.predict(final_features)

        return render_template('result.html', prediction_text=prediction)

        #return render_template('success.html')
    #return render_template('index.html', message='You have already submitted the information for your city')

    
if __name__ == "__main__":
    app.run(debug=True)
