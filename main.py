import requests
import urllib.parse
from flask import Flask, redirect

app = Flask(__name__)
app.secret_key = 'c7869f931c096b1a3cd7c61ae1dd5fdd'

CLIENT_ID = '7a805b18766647f8809cd01d57acff26'
CLINET_SECRET = '7c470252e9004e03b0782b976b77df2f'
REDIRECT_URL = 'http://google.com/callback/'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

@app route('/')
def index():
    return "Welcome to my Spotifyy App <a href='/login'>Login with Spotify</a>"
@app route('/login')
def login():
    scope = 'user_read-private user-read-email'

    params = {
        'clinet_id' :CLINET_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True

    } 

    auth_url = f"{AUTH_URL}?{urlib.parse.urlencode(params)}"

    return redirect(auth_url)





