# Postman-bs
Trying out Postman

Overview
This Flask application sets up a simple web server with several routes. The server has a global variable elapsed which is used in different routes to demonstrate variable handling and HTTP methods in Flask.

Code Breakdown
python
Copy code
from flask import Flask, request

app = Flask(__name__)
Imports: Imports the Flask class and request object from the flask module. Flask is used to create the application instance, and request is useful for handling HTTP requests (though it’s not used in this snippet).

Application Instance: Creates an instance of the Flask application. app is the Flask application object.

python
Copy code
# Initialize elapsed as a global variable
elapsed = 32
Global Variable: Initializes a global variable elapsed with a value of 32. This variable is used to demonstrate data that can be accessed and modified by different routes.
python
Copy code
@app.route('/')
def hello_world():
    return "Hello World"
Root Route (/): Defines a route for the root URL (/). When accessed with a GET request, it returns the string "Hello World".
python
Copy code
@app.route('/gojo')
def gojo():
    return f"Greatly done {elapsed}"
GET Route (/gojo): Defines a route for the URL /gojo. When accessed with a GET request, it returns a string "Greatly done" followed by the current value of the elapsed variable.
python
Copy code
@app.route('/gojo/<int:age>', methods=['GET'])
def gojo_age(age):
    return f"Greatly done2 {elapsed}"
GET Route with Path Parameter (/gojo/<int:age>): Defines a route for the URL /gojo/<age> where <age> is an integer. When accessed with a GET request, it returns a string "Greatly done2" followed by the current value of the elapsed variable. Note that the age parameter is included in the URL but not used in the response.
python
Copy code
@app.route('/gojo/<int:age>', methods=['POST'])
def gojo_post(age):
    global elapsed
    elapsed = age
    return f"Greatly done3 {elapsed}"
POST Route with Path Parameter (/gojo/<int:age>): Defines a route for the URL /gojo/<age> where <age> is an integer. When accessed with a POST request, it updates the global elapsed variable to the value of age and returns a string "Greatly done3" followed by the updated value of elapsed.
python
Copy code
if __name__ == "__main__":
    app.run()
Main Check: This block ensures that the Flask application runs only if the script is executed directly (not imported as a module). The app.run() method starts the Flask development server.
Key Points
Routing: Defines routes for different URLs and HTTP methods (GET and POST).

Global Variable: Uses a global variable elapsed to store and display a value across different routes.

Request Methods: Demonstrates handling different HTTP methods for the same URL pattern. Specifically, GET and POST methods are used for the /gojo/<age> route.

Type Conversion: Uses Flask’s route parameter converters (<int:age>) to ensure the age parameter is treated as an integer.
