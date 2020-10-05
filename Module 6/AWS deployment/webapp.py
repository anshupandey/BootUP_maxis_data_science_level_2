# create a webserver using flask
from flask import Flask, request, render_template
import joblib
import pandas as pd
import json
import numpy as np

#create an app using Flask
app = Flask(__name__)

#load the pickle files
model = joblib.load("churn_prediction.pkl")

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
    # internation plan = no = 0 and yes = 1
    # vmail_messages = normal_user = 001, no vm plan = 010, HFu - 100
    df = pd.DataFrame(data_dict,index=[0])
    intcols = ['Number vmail messages', 'Total day minutes','Total eve minutes', 'Total night minutes',
               'Total intl minutes','Customer service calls']
    for k in intcols:df[k] = df[k].apply(int)
    df['International plan'] = np.where(df['International plan']=="Yes",1,0)
    df['vmail_messages'] = pd.cut(df['Number vmail messages'],bins=[0,1,30,200],
                                  labels=['No VM plan','Normal Users','High Frequency users'],
                                  include_lowest=True)
    df.drop(['Number vmail messages'],axis=1,inplace=True)
    df['HFU'] = np.where(df['vmail_messages']=="High Frequency users",1,0)
    df['NU'] = np.where(df['vmail_messages']=="Normal Users",1,0)
    df['NVP'] = np.where(df['vmail_messages']=="No VM plan",1,0)
    df = df[['HFU','NVP','NU','International plan', 'Total day minutes',
             'Total eve minutes', 'Total night minutes', 'Total intl minutes',
             'Customer service calls']]
    return df
    
if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=8080)