import configparser

config=configparser.RawConfigParser()
config_path="/Users/shishirjoshi/PycharmProjects/PythonProject/nopcommerceApp/Configurations/config.ini"
config.read("config_path")
if not config.read(config_path):
    raise FileNotFoundError(f"Config file not found: {config_path}")

class ReadConfig:
    @staticmethod
    def get_application_url():
        url=config.get('common info','base_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
print(ReadConfig.get_application_url())


