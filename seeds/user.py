from src.dependencies import get_password_hash
from seeds.dependencies import print_model_details

def seed_users(db, model, count):
  print(f"Seeding {count} users :")
  for i in range(1, count+1):
    user = model(
      email=f"user_{i}@example.com",
      hashed_password=get_password_hash('password'))
    db.add(user)
    print_model_details(user, exclude=['hashed_password'])
  db.commit()
  print("Seeding User complete!\n")
