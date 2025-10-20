"""
Proszę napisać generator read_lines(path), który czyta plik linia po liniii zwraca tylko te, które nie są puste.
"""

def read_lines(path):
    with open(path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                yield stripped_line

for line in read_lines('tekst.txt'):
    print(line)