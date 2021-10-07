# Sanic API
 
A Python web-server implemented with Sanic.

# How to run the code
* Create a virtual environment: `virtualenv .venv`
* source it: `. .venv/bin/activate`
* Install dependencies - `pip install -r requirements.txt`
* Run: `python sanic_app.py` (The server runs on localhost, port 8888)

# How to test
* Use the same virtual environment as above
* pytest `test_normalization.py` (Currently only the normalization part is being tested)