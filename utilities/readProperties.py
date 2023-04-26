import configparser

config = configparser.RawConfigParser()
# get the relative path of config file
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password



