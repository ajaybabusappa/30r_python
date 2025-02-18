#Decorators - These are also functions

def example_decorator(func):
    def wrapper():
        print("Check A4 sheets")
        print("Check cartridge")
        func()
        print("Thank you")
    return wrapper


@example_decorator
def printer():
    print("Printing in progres........")

printer()




#Inbuilt functions
# str="Being Human"
# print(str.replace('Human','Salman'))
# print(str)
list =[1,2,3,4]
list.remove(2)
print(list)
list1=[1,2,3,3,4,5]
list1.remove(3)
print(list1)
# list1.remove(6)
print(list1)
# case changing
str="virat kohli"
x=str.upper()
print(x)
str2="VIRAT KOHLI 81"
Y=str2.lower()
print(Y)


