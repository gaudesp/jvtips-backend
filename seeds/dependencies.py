from src.database import engine, Base

def reset_database():
  print("Resetting the database...")
  Base.metadata.drop_all(bind=engine) 
  Base.metadata.create_all(bind=engine)
  print("Database reset complete!\n")

def print_model_details(model_instance):
  attributes = vars(model_instance)
  attributes.pop('_sa_instance_state', None)
  attribute_str = ', '.join([f"{key}='{value}'" for key, value in attributes.items()])
  print(f"- Create <{model_instance.__class__.__name__} {attribute_str}>")
