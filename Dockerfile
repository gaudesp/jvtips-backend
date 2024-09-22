FROM python:3.12.0

WORKDIR jvtips-backend

RUN curl -o /jvtips-backend/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x /jvtips-backend/wait-for-it.sh

COPY seeds /jvtips-backend/seeds
COPY src /jvtips-backend/src
COPY requirements.txt /jvtips-backend/requirements.txt
COPY .env /jvtips-backend/.env

RUN pip install -r requirements.txt
