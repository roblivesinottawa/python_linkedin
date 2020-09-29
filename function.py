def func1():
    print("I am a function")


func1()

# #############################


def func2(arg1, arg2):
    print(arg1 * arg2)


func2(2, 2)

# ############################


def cube(x):
    return x*x*x


cube(10)
print(cube(10))

# ############################


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


print(power(10, 2))
print(power(x=2, num=5))


#
