# #         super keyord in python


# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("You are in the class a")
# class b(a):
#     def __init__(self):
#         super().__init__()
#         print("B")
#     def display():
#         print("you are in the class b")
# class c(b):
#     def __init__(self):
#         super().__init__()
#         print("C")
#     def display():
#         print("you are in the class c")
# obj=c()



#           polymorphism



# def add(a,b,c=0):
#     print(a+b+c)
# add(1,4)
# add(1,2,3)



class animal():
    def sound(self):
        print("animal will make sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
class bird(animal):
    def sound(self):
        print("Bird will sing")
b1=bird()
b1.sound()
