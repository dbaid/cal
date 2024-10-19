class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://steven:xxxxxx@10.81.144.3:3306/cal'
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/demo'


class ProductionConfig(Config):
    pass


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}