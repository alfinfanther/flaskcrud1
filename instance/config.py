import configparser
config_parser = configparser.ConfigParser()
config_parser.read('config.ini')

SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}/{3}'.format(
        config_parser['DB']['DB_USER'],
        config_parser['DB']['DB_PASS'],
        config_parser['DB']['DB_HOST'],
        config_parser['DB']['DB_NAME']
    )

