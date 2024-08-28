from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

global elapsed 
elapsed = 32

@app.route('/gojo')
def gojo():
    return f"Greatly done {elapsed}"

@app.route('/gojo/<age>')
def gojo_age(age):
    return f"Greatly done2 {elapsed}"

@app.route('/gojo/<age>', methods = ['POST'])
def gojo_post(age):
    global elapsed
    elapsed = age
    return f"Greatly done3 {elapsed}"
    

if __name__ == "__main__":
    app.run()
