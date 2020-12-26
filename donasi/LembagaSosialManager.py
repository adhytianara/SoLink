from donasi.LembagaSosialModel import LembagaSosialModel

class LembagaSosialManager:
    __instance = None

    @staticmethod
    def getInstance():
        if LembagaSosialManager.__instance == None:
            LembagaSosialManager()
        return LembagaSosialManager.__instance

    def __init__(self):
        if LembagaSosialManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            LembagaSosialManager.__instance = self