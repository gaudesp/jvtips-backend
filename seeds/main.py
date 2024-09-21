import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from src.database import SessionLocal
from src.user.models import User
from src.guide.models import Guide
from src.game.models import Game

from seeds.user import seed_users
from seeds.game import seed_games
from seeds.guide import seed_guides
from seeds.dependencies import reset_database

def main():
  print(f"Runing Seeds...\n")
  reset_database()
  db = SessionLocal()
  try:
    seed_users(db, User, 10)
    seed_games(db, Game, 25)
    seed_guides(db, Guide, 50)
    print("Seeding complete! For information, the password for all users is 'password'.")
  except Exception as e:
    print(f"An error occurred: {e}")
    db.rollback()
  finally:
    db.close()

if __name__ == "__main__":
  main()
