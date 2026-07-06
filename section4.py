# print("hoooo")

# i=10
# while(i>0):
#     print(i,end=",")
#     i=i-1


# i=int(input('Enter a number: '))
# fact=1
# while(i>0):
#     fact=fact*i
#     i=i-1
# print(fact)




#                python collections



# #a[]     this is list
# a=[1,2,3,4,5]
# b=[7,8,9,10]
# a.extend(b)
# a.insert(1,99)
# a[1]=67
# a.pop(4)
# print(a)
# a.append(6)
# print(a)


# a=()    this is tuple
# a=(1,2,3,4,5)
# b=list(a)
# b.pop(2)
# print(b)


# a={}   this is set
# a={1,2,3,4,1}
# a.add(7)
# a.remove(1)
# a.pop()
# print(a)


# a={
#     this is dictionary
# }
# a={
#     "name":"key",
#     "age":21,
#     "location":"udumalpet",
#     "std":["12th"]
# }
# a["age"]=45
# a.update({"location":"chennai"})
#a.pop("Age")
# del a["std"]
# a["colour"]="blue"
# a.clear()
# print(a)


#         function in python


# def painter():
#     print("painting")
# painter()


# def add():
    # print("Addition")
    # a=int(input("Enter the first number:"))
    # b=int(input("Enter the second number:"))
    # print("a+b")
# add()
# def sub():
    # print("Substraction")
    # a=int(input("Enter the first number:"))
    # b=int(input("Enter the second number:"))
    # print("a-b")
# sub()
# def mul():
    # print("Multipulication")
    # a=int(input("Enter the first number:"))
    # b=int(input("Enter the second number:"))
    # print(a*b)
# mul()
# def div():
    # print("division")
    # a=int(input("Enter the first number:"))
    # b=int(input("Enter the second number:"))
    # print(a/b)
# div()



# def painter(msg):
#     print("Message:",msg)
# painter("Can you paint my house")



# def findevenorodd(b):
#     if(b%2==0):
#         print("This number is even")
#     else:
#         print("This number is odd")
# num=int(input("Enter a number:"))
# findevenorodd(a)



# def num(b):
#     print(b)
# a=67
# num(a)




# def findpassorfail(b):
#     if(b<35):
#         print("You are  fail in the subject")
#     else:
#         print("You are pass in the subject")
# a=int(input("Enter the mark:"))
# findpassorfail(a)



# def numberrange():
#     a=int(input("Enter the first number:"))
#     b=int(input("Enter the second number:"))
#     for i in range(a,b):
#         print(i,end=",")
# numberrange()


def number(a,b):
    for i in range(a,b):
        print(i,end=",")
number(6,11)