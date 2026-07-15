#            Encapsulation



# class company():
#     def __init__(self):
#         self._companyname="google"
# class b(company):
#     pass        
# b1=b()
# print(b1._companyname)




#          exception handling


#   ther are three type of erro
#       -comiple time error
#       -logical error
#       -run time error


# try:
#     a=int(input("Enter a number"))
#     b=int(input("Enter a number"))
#     print(a+b)
# except Exception as e:
#     print("something is wrong",e)



# try:
#     a=int(input())
#     b=int(input())
#     c=input()
#     print(c/a)
#     print(d)
# except ValueError as e:
#     print("something is wrong",e)
# except TypeError as e:
#     print("Somethin is go in correct",e)
# except Exception as e:
#     print("There are some problem in it",e)



# try:
#     a=int(input())
#     b=int(input())
#     print(a-b)
# except Exception as e:
#     print("Something is wrong",e)
# finally:
#     print("all are done")



#       file handling



# f=open("fruits.txt")
# content=f.read()
# print(content)


# f=open("fruits.txt","w")
# f.write("apple\n")
# f.write("mango")
# f.close
# f=open("fruits.txt","r+")
# print(f.read())




# f=open("fruits.txt","a")
# f.write("banna\n")
# f.write("dragonfruits")
# f.close
# f=open("fruits.txt","r+")
# print(f.readline())
