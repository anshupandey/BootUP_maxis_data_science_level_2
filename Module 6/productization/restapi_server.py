# create a webserver using flask
from flask import Flask, request
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
    data = request.data
    #data = dict(data)
    data = json.loads(data.decode())
    print(data,type(data))
    for i in list(data.keys()): print(type(data[i]))
    df = preprocess(data)
    predictions = model.predict(df)
    predictions = [int(i) for i in list(predictions)]
    output = {"predictions":predictions}
    output = json.dumps(output)
    return output



def preprocess(data_dict):
    df = pd.DataFrame(data_dict)
    df['vmail_messages'] = pd.cut(df['Number vmail messages'],bins=[0,1,30,200],
                                 labels=['No VM plan','Normal Users','High Frequency users'],
                                 include_lowest=True)
    df.drop(['Number vmail messages'],axis=1,inplace=True)
    

    df = df[['International plan', 'vmail_messages', 'Total day minutes',
           'Total eve minutes', 'Total night minutes', 'Total intl minutes',
           'Customer service calls']]
    print(df.info())
    # preprocessing data for onehotencoding
    df = preprocessor.transform(df)
    return df
    
if __name__=="__main__":
    app.run(debug=True)