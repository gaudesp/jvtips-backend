from seeds.dependencies import print_model_details
from src.user.models import User as UserModel
from src.game.models import Game as GameModel

def seed_guides(db, guide_model, total):
  print(f"Seeding {total} guides :")
  users = db.query(UserModel).all()
  games = db.query(GameModel).all()
  for i in range(1, total+1):
    guide = guide_model(
      title=f"Guide {i}",
      description=f"This is the description for Guide {i}",
      content=f"Content of Guide {i}",
      game_id=games[i % len(games)].id,
      user_id=users[i % len(users)].id
    )
    db.add(guide)
    print_model_details(guide)
  db.commit()
  print("Seeding Guide complete!\n")
