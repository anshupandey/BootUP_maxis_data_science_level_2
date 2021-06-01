from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    return "Hello from Flask"
    
@app.route("/predict",methods=['GET','POST'])
def main2():
    return "Hello from ML model - telecom churn prediction"

if __name__=="__main__":
    app.run(debug=True)