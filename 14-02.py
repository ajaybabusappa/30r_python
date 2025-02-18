from functools import reduce


l_func = lambda x, y, z: x * y * z
print(l_func(2, 5, 6))

l_func = [1, 2]

#Use case of lambda function
#Generally used in higher order functions
#Map, filter and reduce

def mul_with_five(x):
    return x * 5




print(list(map(lambda x: x * 6, [1, 4, 62, 0, 9])))

print(list(map(lambda y : y * 5, [1, 4, -9])))


#Filter

def check_neg_num(x):
    # if x < 0:
    #     return True
    # return False
    return x < 0

print(list(filter(lambda x: x % 2 == 0, [-2, -3, -1, 22, 13, 15])))


#Reduce - 

print(reduce(lambda x, y: x * y, [1, 5, 9, 11, -12, 15]))



#Scope -  Global and Local scope



num1 = 10

def check():
    num2= 55
    num1 = 25
    print(num2)
    print(num1)


check()
print(num1)
