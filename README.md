# JVTips Backend

REST API project using fastApi.

## Requirements

- [Docker](https://docs.docker.com/engine/install/)

## Running the Application

```bash
sudo bash run.sh
```

## Accessing the Application Locally

- The application will be available at: [http://127.0.0.1:3000](http://127.0.0.1:3000)
- Swagger Documentation: [http://127.0.0.1:3000/docs](http://127.0.0.1:3000/docs)
- Redoc Documentation: [http://127.0.0.1:3000/redoc](http://127.0.0.1:3000/redoc)
- Database Adminer: [http://127.0.0.1:9000](http://127.0.0.1:9000)

## Environment variables

```bash
DATABASE_URL=postgresql://user:password@db:5432/database
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
