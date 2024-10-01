# JVTips Backend

REST API project using fastApi.

## Requirements
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Running the Application

Default running :
```bash
docker compose up --build
```

Running with seeds :
```bash
SEEDS=true docker compose up --build
```

## Accessing the Application Locally

- The application will be available at: [http://localhost:3000](http://localhost:3000)
- Swagger Documentation: [http://localhost:3000/docs](http://localhost:3000/docs)
- Redoc Documentation: [http://localhost:3000/redoc](http://localhost:3000/redoc)
- Database Adminer: [http://localhost:9000](http://localhost:9000)

## Environment variables

```python
POSTGRES_USER=user # postgresql user name
POSTGRES_PASSWORD=password # postgresql user password
POSTGRES_DB=database # postgresql database name
POSTGRES_PORT=5432 # postgresql database port
POSTGRES_HOST=db # db for Docker, localhost for local
ALLOWED_HOSTS=http://localhost:5173 # allow frontend
IGDB_CLIENT_ID = # igdb client id
IGDB_CLIENT_SECRET = # igdb client id
IGDB_API_URL = https://api.igdb.com/v4/games # igdb api url

```

## Project Structure

This structure is inspired by [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)

```ruby
jvtips-backend
├── src
│   ├── module
│   │   ├── config.py  # local configs
│   │   ├── dependencies.py # module dependencies
│   │   ├── models.py  # db models
│   │   ├── router.py  # module endpoints
│   │   ├── schemas.py  # pydantic models
│   │   ├── services.py # service layer for business logic
│   │   └── repositories.py # repository pattern for db transaction
│   ├── config.py  # global configs
│   ├── database.py  # db connection related stuff
│   ├── dependencies.py  # global dependencies
│   ├── main.py  # main app
│   └── router.py #  global router
└── .env # env variables
```
