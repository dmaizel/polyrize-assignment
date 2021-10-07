# Sanic API
 
A Python web-server implemented with Sanic.

# How to run the code
* Create a virtual environment: `virtualenv .venv`
* source it: `. .venv/bin/activate`
* Install dependencies - `pip install -r requirements.txt`
* Run: `python sanic_app.py` (The server runs on localhost, port 8888)
* Login: Send a `POST` request to `/auth` with a valid username and password (can be taken from user.json)
* You can access the `/normalize` endpoint only if you have a valid JWT token(which you should have from the previous step)

# How to test
* Use the same virtual environment as above
* pytest `test_normalization.py` (Currently only the normalization part is being tested)