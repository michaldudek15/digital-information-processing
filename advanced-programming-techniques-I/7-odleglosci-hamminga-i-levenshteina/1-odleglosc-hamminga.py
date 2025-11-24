def hamming(pierwszeSlowo, drugieSlowo):
    odleglosc = 0
    for i in range(len(pierwszeSlowo)):
        if pierwszeSlowo[i] != drugieSlowo[i]:
            odleglosc += 1

    print(f"odległość Hamminga między tymi słowami wynosi: {odleglosc}")


while(True):
    pierwszeSlowo = input("pierwsze słowo: ")
    drugieSlowo = input("drugie słowo: ")
    
    if len(pierwszeSlowo) == len(drugieSlowo):
        break
    else:
        print("słowa muszą mieć taką samą długość")
        continue

hamming(pierwszeSlowo, drugieSlowo)
