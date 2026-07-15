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



# class animal():
#     def sound(self):
#         print("animal will make sound")
# class dog(animal):
#     def sound(self):
#         print("Dog barks")
# class bird(animal):
#     def sound(self):
#         print("Bird will sing")
# b1=bird()
# b1.sound()


# class shape():
#     def area(self):
#         return 0
# class rectangle(shape):
#     def area(self):
#         l=int(input("Enter a number"))
#         b=int(input("Enter a number"))
#         print(l*b)
# r1=rectangle()
# r1.area()


# class person():
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self, name,grade):
#         super().__init__(name)
#         self.grade=grade
#     def display(self):
#         print(self.name,self.grade)
# s1=student("rahul","A")
# s1.dispaly()


# class vehile():
#     def start(self):
#         print("vechile started")
# class car(vehile):
#     def start(self):
#         print("car started")
# c1=car()
# c1.start()


class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manger(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print(self.name,self.salary,self.department)
m1=manger("rahul","150000","ece")
m1.display()

        