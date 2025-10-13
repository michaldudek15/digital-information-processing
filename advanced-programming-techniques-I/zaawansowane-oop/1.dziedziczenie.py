"""
Zaprojektuj hierarchię w stylu: device - phone - smartphone

Każda klasa ma mieć konstruktor i __str__

Smartphone.install_app("X") dodaje aplikację do listy
"""

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"urządzenie: {self.brand} {self.model}"

class Phone(Device):
    def __init__(self, brand, model, sim_card):
        super().__init__(brand, model)
        self.sim_card = sim_card

    def __str__(self):
        return f"telefon: {self.brand} {self.model}, karta SIM: {self.sim_card}"

class Smartphone(Phone):
    def __init__(self, brand, model, sim_card):
        super().__init__(brand, model, sim_card)
        self.apps = []

    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"zainstalowano aplikację: {app_name}")

    def __str__(self):
        return f"Smartfon: {self.brand} {self.model}, karta SIM: {self.sim_card}, aplikacje: {self.apps}"

device1 = Device("Generic", "ModelX")
print(device1)
phone1 = Phone("Nokia", "3310", "123-456-789")
print(phone1)
smartphone1 = Smartphone("Apple", "iPhone 13", "987-654-321")
smartphone1.install_app("Calzy")
print(smartphone1)
