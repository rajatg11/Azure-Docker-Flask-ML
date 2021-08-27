from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib


app = Flask(__name__)

ml_model = joblib.load("titanic_model.pkl")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    #print("I was here 1")
    if request.method == 'POST':
        print(request.form.get('Sex'))
        try:
            Sex = float(request.form['Sex'])
            Age = float(request.form['Age'])
            SibSp = float(request.form['SibSp'])
            Parch = float(request.form['Parch'])
            Pclass = float(request.form['Pclass'])
            pred_args = [Sex, Age, SibSp, Parch, Pclass]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1, -1)
            model_prediction = ml_model.predict(pred_args_arr)
            if model_prediction == 0:
                final_result = "Not Survived"
            else:
                final_result = "Survived"
        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('predict.html', prediction = final_result)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
