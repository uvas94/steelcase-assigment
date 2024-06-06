from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
app = Flask(__name__)

def dataPreprocessing(data):
    cat_feat = data.select_dtypes(exclude=['int', 'float'])

    le = LabelEncoder()
    # Label categorical feat 
    for col in cat_feat.columns: 
        data[col] = le.fit_transform(data[col])
        
    #  curated_df.describe()

    # Use log transform to remove skewness from the data
    skewed_feat = ["Runtime (mins)", "Num Votes"]

    for col in skewed_feat:
        data[col] = np.log(data[col] + 1)
    return data

def scorePrediction(data):
    # Load the trained model and do a prediction
    data = np.array(data).reshape(1, 6)
    print(data)
    df = pd.DataFrame(data=data[0:,0:],
                      columns=["Title", "Runtime (mins)", "Genres", "Num Votes", "Release Date", "Directors"])
    print(df)
    with open('model_v1.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict( dataPreprocessing(df) )

@app.route("/")
def home():
    html = "<a href='/predict'> Predict the IMDb Score of a movie</a>"
    return html.format(format)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    "Predicts the IMDb score of a movie"
    if request.method == "POST":
        data = request.form.to_dict()
        data = list(data.values())
        score = scorePrediction(data)
        return render_template("predict.html", score = score)
    if request.method == "GET":
        return render_template("predict.html") 


if __name__ == '__main__':
    app.run(debug=True)