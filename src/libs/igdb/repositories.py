import requests
from src.config import IGDB_CLIENT_ID, IGDB_API_URL
from src.libs.igdb.dependencies import get_access_token
from src.libs.igdb.schemas import IgdbSearchGames, IgdbGame

class IgdbRepository:
  def __init__(self):
    self.headers = {
      'Authorization': f'Bearer {get_access_token()}',
      'Client-ID': IGDB_CLIENT_ID,
    }

  def find_all(self, query: str) -> IgdbSearchGames:
    data = f'search "{query}"; fields name, category, cover.image_id; where category = 0;'
    return requests.post(IGDB_API_URL, headers=self.headers, data=data)

  def find_by_igdb_id(self, igdb_id: int) -> IgdbGame:
    data = f'fields name, cover.image_id; where id = {igdb_id};'
    return requests.post(IGDB_API_URL, headers=self.headers, data=data)
