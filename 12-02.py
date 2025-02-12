#Functions
#Parameters and arguments
#Positional arguments
#Keyword arguments
#Default arguments
#return statements 

#Arbitrary arguments
#Keyword arbitrary arguments
#Key A.A



from functools import reduce


def example_function(a, b, pie = 3.14, r = 10):
    print("Good morning")
    print("Good morning1")
    print("Good morning2")
    print("Good morning3")
    print("Good morning Radhiak")
    #print(2 + 3)
    print(a)
    print(b)
    if 5 > 2:
        return a - b, a+ b, a * b, a / b
    print(pie)
    print(pie * r * r)

# #Someother operations

res1 = example_function( b = 2, a = 5, r = 10, pie = 2.14)
res = example_function(2, 5,10)

print(res)
print(res1)
# #Someother operations

# example_function(11, 16)

# #Someother operations3


def even_or_odd(num1):
    if num1 % 2 == 0:
        return "Even"

    return "Odd"
    
print(even_or_odd(25))


# def sum(a, b, c):
#     return a + b + c

# def sum1(a, b, c, d):
#     return a + b + c + d


# def sum2(a, b, c, d, e):
#     return a + b + c + d + e

#Arbitrary arguments

# sum(2, 4, 5)
# sum(2, 4, 5, 6)



def sum(a, *b):
    res = a
    for k in b:
        res  += k
    return res
    

sum(5,6, 7, 8, 9, 10, 11, 12, 13)


def sum (**kargs):
    print(type(kargs))
    #print(kargs)
    res = 0
    for i, j in kargs.items():
        res += j
    return res


sum(num0 = 5,num1 = 6, mum2 = 7, num3 = 8, num4 = 9, num5 = 10)




#username, password, gender, dob, remarks, country

#output - Username : ""
#password - ""

#Types of functions
#VOID Functoins
#Functions with return statements

#Void functions
def random_print():
    print("This is just to print")


#Lambda functions - single line, optimisation, anonynmous


lam_example = lambda x, y, z : x + y + z
print(lam_example(5, 6, 7))
print(lam_example(5, 11, 12))

lam_example = 5

# print(lam_example(5, 6, 7))


lam = lambda : "Hello world"
print(lam())

def sum_of_3(x, y, z):
    return x + y + z


#map(func, iterable)

def square(x):
    return x * x * x

def cube(x):
    return x ** 3

res_map = map(lambda x: x - 2, [1, 2, 3, 45, 72, -1])
print(list(res_map))


res_map1 = map(square, [1, 22, 32, 4, 7, -1])
print(list(res_map1))

# print(range(0, 10))
