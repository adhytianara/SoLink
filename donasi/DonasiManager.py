from donasi.DonasiModel import DonasiModel

class DonasiManager:
    __instance = None

    @staticmethod
    def getInstance():
        if DonasiManager.__instance == None:
            DonasiManager()
        return DonasiManager.__instance

    def __init__(self):
        if DonasiManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DonasiManager.__instance = self