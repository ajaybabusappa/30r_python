#Control statements - Controls flow of execution of a code
#Control statements - Conditional statements, Loops and Jump statements

#Conditional statements

num1 = -1
# if num1 == 1:
#    print ("Pushpa The Rise")
# else:
#     print("Pushpa The Rule")
#     print("1500 cr")

# print("Code ended")

#If num2 > 0 then print positive else print negative

# if num1  > 0:
#     if num1 == 1:
#         print("One")
#     else:
#         print("Positive")
# else:
#     if num1 == 0:
#         print("Zero")
#     else:
#         if num1 == -1:
#             print("-1")
#         else:
#             print("Negative")

#else if  - elif

#Way1 
if num1 > 1:
    print("Positive")
elif num1 == 1:
    print("One")
elif num1 == 0:
    print("Zero")
elif num1 == -1:
    print ("-1")
elif num1 == -1:
    print ("-Negative Number")
else:
    print("Negative")

#Way 2
if num1 > 0 and num1 != 1:
    print("Positive")
elif num1 == 1:
    print("One")
elif num1 == 0:
    print("Zero")
elif num1 == -1:
    print ("-1")
elif num1 == -1:
    print ("-Negative Number")
else:
    print("Negative")

#Way3
if num1 == 1:
    print("One")
elif num1 > 0:
    print("Positive")
elif num1 == 0:
    print("Zero")
elif num1 == -1:
    print ("-1")
elif num1 == -1:
    print ("-Negative Number")
else:
    print("Negative")


#Way 4
if num1 > 0:
    if num1 == 1:
        print("One")
    else:
        print("Positive")
elif num1 == 1:
    print("One")
elif num1 == 0:
    print("Zero")
elif num1 == -1:
    print ("-1")
elif num1 == -1:
    print ("-Negative Number")
else:
    print("Negative")


#Current bill
#100 units - Per unit 50 rupees
#101 to 200 - Per unit 100 rupees
#201 to Anynumber - Per unit 150 rupees
#If 0 to 50 - Per unit 0 rupees

current_units = int(input("Enter units"))



if current_units <= 100:
    if current_units < 0:
        print ("Invalid")
    else:
        if current_units <= 50:
            print ("Jai Electricty board")
        else:
            print (current_units * 50)
else:
    if current_units < 201:
        print (current_units * 100)
    else:
        print (current_units * 150)





#Loops -  
print ("Python")
print ("Python")
print ("Python")
print ("Python")
print ("Python")
print ("Python")
