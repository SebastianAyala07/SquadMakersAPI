FROM python:3.8.5-alpine
COPY . /squadmakersapi
WORKDIR /squadmakersapi
ENV FLASK_APP="entrypoint:app"
ENV CHUCK="https://api.chucknorris.io/"
ENV DAD="https://icanhazdadjoke.com/"
ENV FLASK_ENV="development"
ENV APP_SETTINGS_MODULE="config.default.Development"
ENV MYSQL_DATABASE_USER="root"
ENV MYSQL_DATABASE_PASSWORD="root"
ENV MYSQL_DATABASE_DB="squadmakers"
ENV MYSQL_DATABASE_HOST="db"
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]