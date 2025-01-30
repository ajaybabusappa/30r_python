#Logical operators and Bitwise operators

#logical - and, or and not
#&& , || , !

print (True  and True)
print (False and True)
print (True and False)
print (False and (True and True and False))
print (True and False)

print ("---Numbers-----")

print (2 and 3)
print (3 and 2)
print (3 and "")
print ("" and 0)
print (-1 and -3)
print (0 and "")
print (False and 45)
print (None and 3)


#Or
print (True or False)
print (False or True)
print (False or (False and True))
print (True and ((False or True) and (True or False)))

print (2 or 3)
print (3 or 2)
print ("" or True)
print (0 or 0 or 1)


#Not operator
print (not True)
print (not False)
print (not (2 or 3))
print(not ("" and 3))


#bitwise operators - &, |, ^, ~, >>, <<

print (4 & 3)
print (12 & 14)
#0100 & 0011 =>  0000 = 0
#1100 & 1110 => 1100 => 12


#Bitwsie or
print ( 12 | 14)
#1100 | 1110 =>  1110 => 14


#Xor operators 
print (12 ^ 14)

#Left shift -  
#Right shift - 


print (3 << 2)
print (3 >> 1)

print (4 << 2)
print (4 >> 2)

print (29 << 1)
print (29 >> 1)



#1010
#10100

#1010 => 0 * 1 + 1 * 2 + 0 * 4 + 1 * 8
#10100 => 0 * 1 + 0 * 2 + 1 * 4 + 0 * 8 + 1 * 16
#2 * (10) => 20


#Right shift
#0011 => 3
#0001 => 1


#001011 => 11
#000101 => 5


#~
print (~13)
print (~15)
print(~26)





print ("I can vote")
print ("I cannot vote")


age = 18

#if my age is >= 18 then print "Vote" or else "i cannot vote"

if age >= 18:
    print('Hurry! Dabbulu istharu')
    print("Jai Democracy")
else:
    print ("Ivvaru...Sad")