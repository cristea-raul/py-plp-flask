import os


class Paths(object):
    """
    Class with paths constants.
    """

    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    DB_DIR = os.path.join(BASE_DIR, 'databases')
    DB_PATH = os.path.join(DB_DIR, 'data.db')


class AppConfig(object):
    DEBUG = True
    SECRET_KEY = 'DEV_KEY'
    USERNAME = 'admin'
    PASSWORD = 'pass'
