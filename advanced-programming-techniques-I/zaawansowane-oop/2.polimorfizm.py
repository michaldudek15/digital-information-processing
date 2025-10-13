"""
Proszę zaimplementować Employee > Developer / Designer / Manager

Każda ma klasa ma mieć metodę work(), wypisującą inną czynność. 
Utworzyć listę obiektów i wywołać work() w pętli.
"""

class Employee:
    def work(self):
        print("pracownik pracuje")

class Developer(Employee):
    def work(self):
        print("programista pisze kod")

class Designer(Employee):
    def work(self):
        print("projektant projektuje interfejsy")

class Manager(Employee):
    def work(self):
        print("menedżer zarządza zespołem")

employees = [Developer(), Designer(), Manager()]

for employee in employees:
    employee.work()