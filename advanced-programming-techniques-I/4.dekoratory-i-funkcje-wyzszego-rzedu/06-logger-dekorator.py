"""
Proszę utworzyć dekorator @logger, który przed wywołaniem funkcji wypisze:
` [LOG] Wywołano funkcję <nazwa> `


@logger
def hello():
    print("Hej!")

[LOG] Wywołano funkcję hello
Hej!
"""

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Wywołano funkcję {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def powitaj():
    print("elo")

powitaj()