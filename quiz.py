# def Calc(currency, *rates):
#     for i in rates:
#         print(currency*i)


# Calc('CAD', 2, 4)


# ###############################

# you have an existing class Simple() that returns the sum of two numbers using its Add(x,y) method. How can you leverage it to
# build another class that calculates the inverse of the sum of two numbers?
# class Advanced(Simple):
#     def Inverse(self, x, y):
#         return(1/Simple.Add(self, x, y))


# ##################################
# a = 1
# b = 2


# def func():
#     global b
#     b = a + b


# func()
# print(b)

# #################################


# class Person:
#     def __initialize__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex


# ####################################

# def inc(a, b=10):
#     return(a+b)


# a = inc(10)
# a = inc(a, a)
# print(a)

# #################################

# you need to set the annual payment in one function and print the respective monthly payment in a separate function. How would you fix the suggested code to work properly?


# def SetAnnual():
#     global annual
#     annual = 70000


# def PrintMonthly():
#     print("Your monthly payment is "+str(annual/12)+" USD.")


# SetAnnual()
# PrintMonthly()


# ##############################################

# max=x if (x>y) else y

# # or

# max = y
# if (x>y):
#     max = x

# ###############################################


# number = 40

# if (number >= 1000):
#     print(4)
# elif (number >= 100):
#     print(3)
# elif (number >= 10):
#     print(2)
# else:
#     print(1)


# ##################################
# def Sum10th(data):
#     sum = 0
#     for i, d in enumerate(data):
#         if (i % 10 == 0):
#             sum = sum+d
#     return sum


# Sum10th()
