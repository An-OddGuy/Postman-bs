# Postman-bs

This is a simple Flask application demonstrating basic routing, handling of HTTP methods, and global variable usage.

## Application Code

```python
from flask import Flask, request

app = Flask(__name__)

# Initialize elapsed as a global variable
elapsed = 32

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/gojo')
def gojo():
    return f"Greatly done {elapsed}"

@app.route('/gojo/<int:age>', methods=['GET'])
def gojo_age(age):
    return f"Greatly done2 {elapsed}"

@app.route('/gojo/<int:age>', methods=['POST'])
def gojo_post(age):
    global elapsed
    elapsed = age
    return f"Greatly done3 {elapsed}"

if __name__ == "__main__":
    app.run()
