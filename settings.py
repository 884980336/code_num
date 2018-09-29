from app import db
class DatabaseSetting:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/go_test?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class SessionSetting:
    SESSION_TYPE = 'sqlalchemy'
    SESSION_SQLALCHEMY = db
    SESSION_SQLALCHEMY_TABLE = 'session'
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = False
    SESSION_KEY_PREFIX = 'session'
    PERMANENT_SESSION_LIFETIME = 1*60*60*24*15


class EmailSetting:
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = False
    MAIL_USERNAME = '884980336@qq.com'
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = '884980336@qq.com'
    # MAIL_SUPPRESS_SEND = True
    # MAIL_DEBUG = True


class UseSetting(DatabaseSetting, SessionSetting, EmailSetting):
    pass
