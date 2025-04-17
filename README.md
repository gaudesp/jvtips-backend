# JVTips Backend 🎮💡
JVTips Backend est une API RESTful développée avec **FastAPI** et **Python**, conçue pour interagir avec l'interface de [JVTips Frontend](https://github.com/gaudesp/jvtips-frontend), permettant de partager des astuces sur des jeux vidéo.

## ⚙️ Prérequis
- **Docker** (*version* : `28.0.1`)
- **Docker Compose** (*version* : `2.33.1`)
- **Python** (*version* : `3.12.0`)
- Un **terminal** compatible **Bash** (*sur WSL ou Unix-like*)
- Le fichier `.env` de configuration (*à récupérer sur le Drive*)

> 💡 **Optionnel**, utilisez un environnement virtuel pour isoler les dépendances :
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Setup
1. **Clonez le repo** :  
```bash
git clone git@github.com:gaudesp/jvtips-backend.git
cd jvtips-backend
```

2. **Lancez l'application avec Docker Compose** :
- Pour lancer l'application sans données préremplies :
```bash
docker compose up --build
```
- Pour lancer l'application avec des données initiales (seeds) :
```bash
SEEDS=true docker compose up --build
```

3. **Accédez à l'application localement** :
- API accessible via : [http://localhost:3000](http://localhost:3000)
- Documentation Swagger : [http://localhost:3000/docs](http://localhost:3000/docs)
- Documentation Redoc : [http://localhost:3000/redoc](http://localhost:3000/redoc)
- Adminer (gestion de la base de données) : [http://localhost:9000](http://localhost:9000)

## 📦 Dépendances
- `fastapi` : Framework principal utilisé pour la création de l'API REST.
- `uvicorn` : Serveur ASGI pour exécuter l'application FastAPI.
- `pydantic` : Utilisé pour la validation des données et des modèles.
- `SQLAlchemy` : ORM pour interagir avec la base de données.
- `psycopg2-binary` : Adaptateur PostgreSQL pour Python.
- `bcrypt` et `pyjwt` : Gestion de la sécurité pour l'authentification des utilisateurs.
- `requests` : Librairie pour interagir avec des API externes.
- `python-multipart` : Pour gérer les fichiers envoyés par l'utilisateur via l'API.

## Contribution 🤝
Lead developer : [@gaudesp](https://github.com/gaudesp)
