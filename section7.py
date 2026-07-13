#              type of class variable


# class phone:
#     charger="c-tyoe"
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def display(self):
#         print("Brand",self.brand)
#         print("price",self.price)
#         print("charger",self.charger)
# samsumg=phone("samsung","12222",)
# iphone=phone("iphone","150000",)
# samsumg.display()
# iphone.display()


#            type of class methods


# class laptop:
#     charger="c-type"
#     def __init__(self):
#         self.brand="" 
#         self.price=45
#     def setprice(self,price):
#         self.price=price
#     def getprice(self):
#         print(self.price)
#     @classmethod
#     def changedcharger(cls):
#         cls.charger="b-type"
#     @staticmethod
#     def info():
#         print("This is the information about the laptop")
# hp=laptop()
# hp.setprice(150000)
# hp.getprice()
# laptop.changedcharger()
# hp.info()

 
#              inheritance and its type



# class dad:
#     def phone(self):
#         print("This is dad phone")
# class mom():
#     def sweet(self):
#         print("This is the sweet cooked by my mom")
# class son(dad,mom):
#     def laptop(self):
#         print("This is the sons laptop")
# ram=son()
# ram.phone()
# ram.sweet()



# class grandpa():
#     def phone(self):
#         print("it is grandpa's phone")
# class dad(grandpa):
#     def money(self):
#         print("dad had a money")
# class son(dad):
#     def laptop(self):
#         print("Son had a laptop")
# ram=grandpa()
# ram.laptop()
# ram.money()
# d1=dad
# d1.phone()
# ram.phone()


# class dad():
#     def phone(self):
#         print("dad had a money")
# class son1(dad):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass
# s1=son1()
# s1.money


# class dad():
#     def money(self):
#         print("Dad had a money")
# class land():
#     def important(self):
#         print("It is some important land")
# class son1(dad,land):
#     pass
# class son2(dad):
#     pass
# s1=son1()
# s1.money()