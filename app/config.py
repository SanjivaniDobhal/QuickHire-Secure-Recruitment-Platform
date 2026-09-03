import os
from urllib.parse import quote_plus


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

    mysql_user = os.environ.get('MYSQL_USER')
    mysql_password = os.environ.get('MYSQL_PASSWORD')
    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_port = os.environ.get('MYSQL_PORT')
    mysql_database = os.environ.get('MYSQL_DATABASE')

    if all([
        mysql_user,
        mysql_password,
        mysql_host,
        mysql_port,
        mysql_database
    ]):
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://"
            f"{quote_plus(mysql_user)}:"
            f"{quote_plus(mysql_password)}@"
            f"{mysql_host}:"
            f"{mysql_port}/"
            f"{mysql_database}"
        )

        SQLALCHEMY_ENGINE_OPTIONS = {
            "connect_args": {
                "ssl": {
                    "check_hostname": True
                }
            }
        }

    else:
        SQLALCHEMY_DATABASE_URI = (
            os.environ.get(
                'SQLALCHEMY_DATABASE_URI',
                'mysql+pymysql://root:@localhost/quick_hire_db'
            )
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False