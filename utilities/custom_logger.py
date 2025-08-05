import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        file_handler = logging.FileHandler("/Users/shishirjoshi/PycharmProjects/PythonProject/nopcommerceApp/Logs/automation.log", mode='a')
        formatter = logging.Formatter(
                '%(asctime)s:%(levelname)s:%(message)s',
                datefmt='%m/%d/%y %I:%M:%S %p'
            )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

        return logger



