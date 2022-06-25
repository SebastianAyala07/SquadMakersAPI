#! /bin/sh
export FLASK_APP="entrypoint:app"
export CHUCK="https://api.chucknorris.io/"
export DAD="https://icanhazdadjoke.com/"
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