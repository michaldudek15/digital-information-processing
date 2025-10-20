# W Pythonie obiekty, po których można „przechodzić” w pętli for, to iterowalne.
# Aby być iterowalnym, obiekt musi implementować metodę __iter__().

# Iterator to obiekt, który faktycznie zwraca kolejne elementy.
# Musi implementować metody: __iter__() (zwraca samego siebie) i __next__() (zwraca kolejny element lub wywołuje  StopIteration).

numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# next(it) -> StopIteration

###############

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

for i in Counter(1, 5):
    print(i)

####################

# GENERATOR

# Zachowuje swój stan między kolejnymi wywołaniami next().

def counter(start, end):
    while start <= end:
        yield start
        start += 1

for i in counter(1, 5):
    print(i)

####################

# Wyrażenie generatorowe

gen = (x * x for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
print(list(gen))  # [4, 9, 16]

####################

####################