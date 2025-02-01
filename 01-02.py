#Jump statements - break, continue and pass

#Break and continue - we use in loops


# for i in range(0, 21):
#     if i == 0:
#         break
#     if i % 2 == 0:
#         print(i)

# for i in range(0, 21):
#     if i == 0:
#         break
#     if i % 2 == 0:
#         print(i)



# for i in range(0, 31):
#     if i == 2 or i == 5:
#         break


#Continue
for i in range(0, 10):
    print(i, "Iteration")
    if i == 5 or i == 6:
        continue

    print(i)





for i in range(0, 20):
    continue
    break



#Break and continue for nested loops

for cls1 in range(1, 11):
    for roll in range(1, 30):
        if cls1 == 3 and roll > 15:
            continue
        print(cls1, roll)


#Pass

num1 = 15

if num1 % 7 == 0:
    pass

else:
    print("Something something")



def example_function():
    pass




#Terinary operator

num1 = 5

num2 = 10

# if num2 % 10 == 0:
#     num1 = 10
# else:
#     num1 = 8



num1 = 10 if num2 % 10 == 0 else 8
print(num1)

time = 13
str1 = "good morning" if time < 12 else "good afternoon"
print(str1)