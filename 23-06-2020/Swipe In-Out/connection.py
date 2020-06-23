import configparser


class DevConfig:
    def __init__(self, loggers):
        try:
            self.db_config = configparser.ConfigParser()
            self.db_config.read('dev.properties')
            self.logger = loggers
        except FileNotFoundError as e:
            print(e)
            self.logger.exception("File Not Found!!!!!")
        except Exception as e:
            print(e)
            self.logger.exception("Exception occurred!!!!!", e)

    def connect_db(self):
        try:
            env = 'dev'
            host = self.db_config.get(env, 'host')
            user = self.db_config.get(env, 'user')
            password = self.db_config.get(env, 'password')
            db = self.db_config.get(env, 'db')
            return host, user, password, db
        except ConnectionError as e:
            print(e)
            self.logger.exception("Connection Error!!!!!")
        except Exception as e:
            print(e)
            self.logger.exception("Exception occurred!!!!!", e)
