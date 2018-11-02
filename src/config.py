import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://username:password@localhost/'
database_name = 'idiomrecommender'


class BaseConfig:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class Development(BaseConfig):
    DEBUG = True


class Production(BaseConfig):
    DEBUG = False


app_config = {
    'development': Development,
    'production': Production,
}
