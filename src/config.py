class Config:
    SECRET_KEY = 'Z!1weNBt1T^%kvhUJ*T^'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'gruvitec_prueba'

config={
    'development':DevelopmentConfig
}