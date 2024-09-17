FROM python:3.12.0
WORKDIR /jvtips-backend
COPY ./src /jvtips-backend/src
COPY requirements.txt /jvtips-backend/requirements.txt
COPY .env /jvtips-backend/.env
RUN pip install -r requirements.txt
