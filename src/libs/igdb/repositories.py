import requests
from src.config import IGDB_CLIENT_ID, IGDB_API_URL
from src.libs.igdb.dependencies import get_access_token
from src.libs.igdb.schemas import IgbdGames

class IgdbRepository:
  def __init__(self):
    self.headers = {
      'Authorization': f'Bearer {get_access_token()}',
      'Client-ID': IGDB_CLIENT_ID,
    }

  def find_games(self, query: str) -> IgbdGames:
    data = f'search "{query}"; fields name, category; where category = 0;'
    return requests.post(IGDB_API_URL, headers=self.headers, data=data)
