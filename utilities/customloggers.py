import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        testlog = logging.getLogger()
        testlog.setLevel(logging.INFO)
        return testlog





