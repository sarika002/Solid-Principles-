class mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_discount(self):
        return self.price*0.2

class Android(mobile):
    def get_discount(self):
        return super().get_discount()*2

class IOS(mobile):
    def get_discount(self):
        return super().get_discount()*1.5

mob=Android("Vivo",20000)
print(mob.get_discount())

Mob=IOS("iphone",60000)
print(Mob.get_discount())
