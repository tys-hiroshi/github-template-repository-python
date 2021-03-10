import logging.config

# def __init__(self, base_path: str, config_file_name: str):
#     self.logging_config_file_path = os.path.join(base_path, config_file_name)

class Logger():
    def __init__(self, config_file_path: str):
        logging.config.fileConfig(config_file_path)
        self.logger = logging.getLogger()

    def info(self, message, console=False):
        if console:
            print(f'[Info] {message}')
        self.logger.info(message)

    def debug(self, message, console=False):
        if console:
            print(f'[Debug] {message}')
        self.logger.debug(message)
