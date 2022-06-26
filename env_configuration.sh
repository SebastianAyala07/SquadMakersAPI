#! /bin/sh
export FLASK_APP="entrypoint:app"
export CHUCK="https://api.chucknorris.io/"
export DAD="https://icanhazdadjoke.com/"
export MYSQL_DATABASE_USER="root"
export MYSQL_DATABASE_PASSWORD="root"
export MYSQL_DATABASE_DB="squadmakers"
export MYSQL_DATABASE_HOST="db"
if [ "testing" = $1 ]; then
    export FLASK_ENV="testing"
    export APP_SETTINGS_MODULE="config.default.Testing"
elif [ "production" = $1 ]; then
    export FLASK_ENV="production"
    export APP_SETTINGS_MODULE="config.default.Production"
elif [ "development" = $1 ]; then
    export FLASK_ENV="development"
    export APP_SETTINGS_MODULE="config.default.Development"
fi