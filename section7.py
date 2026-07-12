#              type of class variable


class phone:
    charger="c-tyoe"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand",self.brand)
        print("price",self.price)
        print("charger",self.charger)
samsumg=phone("samsung","12222",)
iphone=phone("iphone","150000",)
samsumg.display()
iphone.display()
