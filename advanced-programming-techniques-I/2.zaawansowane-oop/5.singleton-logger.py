"""
Proszę stworzyć klasę Logger, która zapisuje logi do pliku, 
ale istnieje (może istnieć) tylko jedna jej instancja.
"""

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename="log.txt"):
        if hasattr(self, 'initialized'):
            print("logger już został zainicjalizowany.")  
        if not hasattr(self, 'initialized'):
            self.filename = filename
            self.initialized = True

    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')

logger1 = Logger("test.log")
logger1.log("to jest testowy komunikat.")

logger2 = Logger("another.log")
logger2.log("to jest inny komunikat.")

# sprawdzenie, czy to ten sam obiekt
print(id(logger1))
print(id(logger2))