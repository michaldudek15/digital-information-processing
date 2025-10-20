"""
Proszę napisać iterator Reversed, który odwraca dowolny ciąg (string lub listę).

for x in Reversed("Python"):
    print(x, end=" ")
# n o h t y P
"""

class Reversed:
    def __init__(self, data):
        self.data = data
        self.letterIndex = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.letterIndex == 0:
            raise StopIteration
        self.letterIndex -= 1
        return self.data[self.letterIndex]

for x in Reversed("Python"):
    print(x, end=" ")