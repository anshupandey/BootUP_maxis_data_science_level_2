# create a webserver using flask
from flask import Flask

#create an app using Flask
app = Flask(__name__)

# use generator to trigger a function whenever a request is received on server
@app.route('/')
def main():
    return "Hey Hi, Hello from Flask"

@app.route('/abc')
def main2():
    return "Hello from ABC"

if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=8080)