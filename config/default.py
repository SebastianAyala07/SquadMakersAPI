import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    TESTING = False
    DEBUG = False
    ERROR_404_HELP = False
    MYSQL_DATABASE_USER = os.getenv("MYSQL_DATABASE_USER")
    MYSQL_DATABASE_PASSWORD = os.getenv("MYSQL_DATABASE_PASSWORD")
    MYSQL_DATABASE_DB = os.getenv("MYSQL_DATABASE_DB")
    MYSQL_DATABASE_HOST = os.getenv("MYSQL_DATABASE_HOST")


class Production(Config):
    PROPAGATE_EXCEPTIONS = False

class Development(Config):
    PROPAGATE_EXCEPTIONS = True

class Testing(Config):
    TESTING = True
