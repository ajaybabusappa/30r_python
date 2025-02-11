#Functions
#Parameters and arguments
#Positional arguments
#Keyword arguments
#Default arguments
#return statements



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
        return a - b
    print(pie)
    print(pie * r * r)

# #Someother operations

res1 = example_function( b = 2, a = 5, r = 10, pie = 2.14)
res = example_function(2, 5,10)

print(res + 5)
# #Someother operations

# example_function(11, 16)

# #Someother operations3


def even_or_odd(num1):
    if num1 % 2 == 0:
        return "Even"

    return "Odd"
    
print(even_or_odd(25))