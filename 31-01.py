# # #For loop and while loop

# # # for y in range(0, 21):
# # #     print(y)
# # #     #print (y + 5)
# # #     # print ("Edho okati")
# # #     # print ("Malli edho okati")


# # # for i in range(5, 26):
# # #     if i % 2 == 0:
# # #         print (i, 'Even')
# # #     else:
# # #         print (i, "Odd")



# # # for i in range(0, 21, 2):
# # #     print (i)


# # for i in range(0, 21, 3):
# #     print (i)

# # for i in range(0, 21):
# #     if i % 3 == 0:
# #         print(i)

# #     print (i * i * i)
# #     print (i ** 2)



# # #Nested loops: 


# # # #1st class
# # # for i in range(1, 31):
# # #     print (i)

# # # #2nd class
# # # for i in range(1, 31):
# # #     print (i)


# # for j in range(1, 11): #j = 1
# #     if j != 5 and j != 7:
# #         for i in range(1, 31):
# #             print (j, i)
# #         # if j != 5 and j != 7:
# #         #     print (j, i)

    

# #While loop
# #while I am going to the home, I was watching a movie
# #Where should I use for loop and where should I use while loop?

# num1 = 4

# while num1 < 5:
#     print ("Kill ...")
#     print ("Still fighting")
#     num1 += 1





# start = 5

# while start < 26:
#     if start % 2 == 0:
#         print (start, "Even")
#     else:
#         print (start, "Odd")
#     start += 1  

# #Converting nested for loops to while loops
# for j in range(1, 11): #j = 1
#     if j != 5 and j != 7:
#         for i in range(1, 31):
#             print (j, i)
#         # if j != 5 and j != 7:
#         #     print (j, i)


j = 1

while j < 11:
    i = 1
    print(i)
    if j != 5 and j != 7:
        while i < 31:
            print (j, i)
            i += 1
    j += 1

