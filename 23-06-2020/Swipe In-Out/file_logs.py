import logging
from os import path


class FileLog:
    def __init__(self, table_name):
        self.logger = logging.getLogger(table_name)

    def logs_handler(self, log_name):
        try:
            file_handler = logging.FileHandler((path.dirname(__file__))+ '\\' + log_name + '.log')
            formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            self.logger.setLevel(logging.INFO)
            return self.logger
        except Exception as e:
            print(e)
            self.logger.exception("Exception occurred!!!!!", e)
