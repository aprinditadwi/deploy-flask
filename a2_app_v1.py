from flask import Flask

# we define a variable called app
app = Flask(__name__) 

# tells Flask what URL a user has to browse to call the function below. 
# you will need to browse the url : '/test'
@app.route("/test")
def test():
    return "First app in Flask"
