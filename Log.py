import os

#used in connect function for exceptions

class Log: 
    @staticmethod      
    def __init__(name = "/BinanceLogFile.txt"):         
        try:
            LogFile = os.getcwd() + name
            Log.filePTR = open(LogFile,"a",encoding="utf-8")
        except Exception as e:
            print(e)
        

    @staticmethod
    def write(message):
        Log.filePTR.write(message + "\n")
