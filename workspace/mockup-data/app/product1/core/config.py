import os

# postgresql connection
POSTGRESQL_SERVER = os.environ['POSTGRESQL_SERVER']
POSTGRESQL_PORT = os.environ['POSTGRESQL_PORT']
POSTGRESQL_USER = os.environ['POSTGRESQL_USER']
POSTGRESQL_PASSWORD = os.environ['POSTGRESQL_PASSWORD']

# datetime format
TIMEZONE = 'Asia/Ho_Chi_Minh'
DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'