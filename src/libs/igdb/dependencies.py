import requests
from fastapi import HTTPException
from src.config import IGDB_CLIENT_ID, IGDB_CLIENT_SECRET

auth_token = None
token_expiration = 0

def authenticate():
  global auth_token, token_expiration
  response = requests.post('https://id.twitch.tv/oauth2/token', params={
      'client_id': IGDB_CLIENT_ID,
      'client_secret': IGDB_CLIENT_SECRET,
      'grant_type': 'client_credentials'
    }
  )

  if response.status_code == 200:
    data = response.json()
    auth_token = data['access_token']
    token_expiration = data['expires_in']
  else:
    raise HTTPException(status_code=response.status_code, detail="Authentication failed")

def get_access_token():
  global auth_token, token_expiration
  if auth_token is None or token_expiration <= 0:
    authenticate()
  
  token_expiration -= 1
  return auth_token
