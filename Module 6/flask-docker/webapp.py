# create a webserver using flask
from flask import Flask, request, render_template
import joblib
import pandas as pd
import json

#create an app using Flask
app = Flask(__name__)

#load the pickle files
model = joblib.load("churn_prediction.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# use generator to trigger a function whenever a request is received on server
@app.route('/',methods=["POST","GET"])
def main():
    return render_template("index.html")

@app.route('/prediction',methods=["POST","GET"])
def main2():
    data = dict(request.form)
    df = preprocess(data)
    prediction = model.predict(df)
    prediction = [int(i) for i in prediction] # converting the boolean to integer
    data["Prediction"] = prediction[0]
    data["Probability"] = model.predict_proba(df)[0][1]
    return render_template("output.html",output=data)


def preprocess(data_dict):
    df = pd.DataFrame(data_dict,index=[0])
    intcols = ['Number vmail messages', 'Total day minutes','Total eve minutes', 'Total night minutes',
               'Total intl minutes','Customer service calls']
    for k in intcols:df[k] = df[k].apply(int)
    df['vmail_messages'] = pd.cut(df['Number vmail messages'],bins=[0,1,30,200],
                                  labels=['No VM plan','Normal Users','High Frequency users'],
                                  include_lowest=True)
    df.drop(['Number vmail messages'],axis=1,inplace=True)
    df = df[['International plan', 'vmail_messages', 'Total day minutes',
             'Total eve minutes', 'Total night minutes', 'Total intl minutes',
             'Customer service calls']]
    # preprocessing data for onehotencoding
    df = preprocessor.transform(df)
    return df
    
if __name__=="__main__":
    app.run(host="0.0.0.0")