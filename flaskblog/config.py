import settings


class Config:
    SECRET_KEY = settings.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI
    MAIL_SERVER = settings.MAIL_SERVER
    MAIL_PORT = settings.MAIL_PORT
    MAIL_USE_SSL = settings.MAIL_USE_SSL
    MAIL_USERNAME = settings.MAIL_USERNAME
    MAIL_PASSWORD = settings.MAIL_PASSWORD
