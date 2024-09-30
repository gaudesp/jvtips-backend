from seeds.dependencies import print_model_details

data = [
  {
    "name": "Waven",
    "igdb_image": "co6y8e",
    "igdb_id": "109536"
  },
  {
    "name": "League of Legends",
    "igdb_image": "co49wj",
    "igdb_id": "115"
  },
  {
    "name": "Artisan TD",
    "igdb_image": "co7l8r",
    "igdb_id": "281796"
  },
  {
    "name": "Minecraft: Java Edition",
    "igdb_image": "co8fu6",
    "igdb_id": "121"
  },
  {
    "name": "Palworld",
    "igdb_image": "co7n02",
    "igdb_id": "151665"
  }
]

def seed_games(db, model, data=data):
  print(f"Seeding {len(data)} games :")
  for item in data:
    game = model(
      name=item['name'],
      igdb_image=item['igdb_image'],
      igdb_id=item['igdb_id']
    )
    db.add(game)
    print_model_details(game)
  db.commit()
  print("Seeding Game complete!\n")
