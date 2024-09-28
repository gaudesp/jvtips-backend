from seeds.dependencies import print_model_details

def seed_games(db, model, count):
  print(f"Seeding {count} games :")
  for i in range(1, count+1):
    game = model(
      name=f"Game {i}",
      igdb_id=109536
    )
    db.add(game)
    print_model_details(game)
  db.commit()
  print("Seeding Game complete!\n")
