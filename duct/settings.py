import os
# pbkdf2 configuration
PASSWORD_SALT = '7Csdd3211A1as31231zZMFdsM'

# open bank authorization
CONSUMER_USERNAME = os.environ["CONSUMER_USERNAME"]
CONSUMER_PASSWORD = os.environ["CONSUMER_PASSWORD"]
CONSUMER_KEY = os.environ["CONSUMER_KEY"]

CALLBACK_URI = 'http://127.0.0.1:5000/welcome'
ODB_BASE_URL = "https://apisandbox.openbankproject.com"