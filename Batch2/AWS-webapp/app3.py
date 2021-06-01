from flask import Flask, request, render_template
import pandas as pd
import joblib
import json

model = joblib.load("model.pkl")
pipeline = joblib.load("pipeline.pkl")

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    return render_template("index.html")
    
@app.route("/predict",methods=['GET','POST'])
def main2():
    data = request.form
    data = dict(data) # convert json to dict
    print(data,type(data))
    pred = process_data(data)
    output = {"Prediction":pred.tolist()}
    return json.dumps(output)

def process_data(data_dict):
    data_dict['Number vmail messages'] = int(data_dict['Number vmail messages'])
    df = pd.DataFrame(data_dict,index=[0])
    df['vmail_messages'] = pd.cut(df['Number vmail messages'],bins=[0,1,30,200],
                             labels=['No VM plan','Normal Users','High Frequency users'],
                             include_lowest=True)
    df = df[['International plan','vmail_messages','Total day minutes','Total eve minutes',
     'Total night minutes','Total intl minutes','Customer service calls']]
    df = pipeline.transform(df)
    predictions = model.predict(df)
    return predictions


if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=8080)