# #Scope - Global, local
# #Global scope
# #Local scope
# #We have also seen global keyword
# #We have seen globals keyword
# #Scope vs Lifetime

# num_1 = 15

# def check_scope():
#     num_2 = 35
#     num_1 = 32
#     globals()['num_1'] = 45
#     print(num_1)
#     #print(num_2)

# check_scope()
# print(num_1)
# #print(num_2)


# #in-build functions
# #count()
# txt = "i am satish , satish coming from home"
# arr = [1,2,2,3,3,4,5, [1, 2, 3]]
# # syntax = variavle.count("value")
# l = txt.count("Satish")
# x = arr.count(3)
# print(l)
# print(x)

# #slicing strings
# #start stop Step

# #ex:
# s1="Hello python"

# print(s1[-1:-4:-1])





#+ join() format() f


# a="hello"
# b="daddy!"

# res="{}, hsdjakls iojlcaskc {}".format(a,b)
# print(res)


# res2=f"{a},{b}"
# print(res2)



# c=[1,2,3]

# print(c*3)

# print(c+c+c)/cls


#strip
 #string.strip(cherecters)
# txt="    pavan     "
# x = txt.strip()
# print(x)

# txt="...gtr..pavan...gtr..."
# x = txt.strip(" ")
# print(x)

a={1,2,3,4,11}
c={11,22,34}
b={111,232,13,11}
d=a&c&b
print(d)

