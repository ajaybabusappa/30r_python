# #Prime Numbers - 2, 3, 5, 7, 11, 13
# #Divisible by 1 and itself - count of factors is 2


# num1 = int(input("Enter a number to check for prime"))

# # #Approach 1 #for 31 - 31 times
# # if num1 in [0, 1] or num1 < 0:
# #     print("Neither prime nor composite")
# # else:
# #     count = 0
# #     for i in range(1, num1 + 1):
# #         if num1 % i == 0:
# #             count += 1

# #     print("Prime") if count == 2 else print("Not prime")




# #Approach 2
# #16 - 2 to 15
# #15
# if num1 in [0, 1] or num1 < 0: # for 31 - 29 times
#     print("Neither prime nor composite")
# else:
#     spy = True
#     for i in range(2, num1):
#         if num1 % i == 0:
#             spy = False
#             print("Not a prime")
#             break
    
#     if spy:
#         print("Prime")

    

# #Approach 3
# #18 - 1, 2, 3, 6, 9, 18
# #22 - 1, 2, 11, 22
# #39 - 1, 3, 13, 39
# #17 - 1, 17
# #54 - 1, 2, 3, 6, 9, 18, 27, 54


# #c = a * b  (a = c, b = 1)
# #c = a * b (a = c/2 , b = 2)


# if num1 in [0, 1] or num1 < 0: #for 31 - 15
#     print("Neither prime nor composite")
# else:
#     spy = True
#     for i in range(2, num1 // 2 + 1):
#         if num1 % i == 0:
#             spy = False
#             print("Not a prime")
#             break
    
#     if spy:
#         print("Prime")



# #Approach 4
# #64
# #1 * 64 = 64
# #2 * 32 
# #4 * 16
# #8 * 8
# #16 * 4
# #32 * 2
# #64 * 1



# #c = m * m


# if num1 in [0, 1] or num1 < 0: #31 - 4 times
#     print("Neither prime nor composite")
# else:
#     spy = True
#     for i in range(2, int(num1 ** 0.5) + 1):
#         if num1 % i == 0:
#             spy = False
#             print("Not a prime")
#             break
    
#     if spy:
#         print("Prime")



#Fibonacci number
#f(n) = f(n-1) + f(n-2) if n == 0 output 0 if n == 1
#0 1 1 2 3 5 8 13 21 34 55 89 144 233


num1, num2 = 0, 1
n = 15
# if n >= 0:
#     print(num1)
# if n >= 1:
#     print(num2)


for i in range(0, 15):
    print(num1)
    temp = num1 + num2
    # print(temp)
    num1 = num2
    num2 = temp

