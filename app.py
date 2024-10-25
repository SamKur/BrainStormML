from flask import Flask, request, render_template
# run => flask --app filename run
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata", methods = ['GET','POST'])
def predict_datapoint():
    print("predict_datapoint route accessed")  # Added print for debugging
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        print("predict_datapoint POST accessed")  # Added print for debugging

        data = CustomData(gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
            )
        print("predict_datapoint before data_df created")  # Added print for debugging
        
        data_df = data.get_data_as_dataframe()
        print(data_df)

        print("Before Prediction")
        predict_pipeline = PredictPipeline()
        print("In Prediction") # after this getting error BUT?
        result = predict_pipeline.predict(data_df)
        print("After Prediction")
        return render_template('home.html', results=result[0])



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)