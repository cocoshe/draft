import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
from fastapi import APIRouter
import base64
import dotenv
import requests

dotenv.load_dotenv()

router = APIRouter()

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_URL = "https://api.spotify.com/v1"

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
print("CLIENT_ID", CLIENT_ID)
print("CLIENT_SECRET", CLIENT_SECRET)
print("REDIRECT_URI", REDIRECT_URI)


@router.get("/auth")
async def auth():
    all_scopes = "user-read-private user-read-email playlist-modify-public playlist-modify-private playlist-read-private user-top-read user-read-recently-played user-read-playback-position user-read-playback-state user-modify-playback-state user-read-currently-playing user-library-read user-library-modify"
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": all_scopes
    }
    return RedirectResponse(SPOTIFY_AUTH_URL + "?" + urlencode(params))


@router.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")

    auth_options = {
        'url': 'https://accounts.spotify.com/api/token',
        'params': {
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'grant_type': 'authorization_code',
        },
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode('utf-8')).decode('utf-8'),
        }
    }
    response = requests.post(auth_options['url'], data=auth_options['params'], headers=auth_options['headers'])
    return JSONResponse(status_code=200, content={"response": response.json()})