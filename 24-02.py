
# sum = 0
# for i in range(1, 101):
#     print(i)
#     sum = sum + i #sum += i

# print(sum)

# n = 15

# print((n * (n + 1)) / 2)


# num1 = int(input("Enter the number"))

# for i in range(1, 21):
#     print(num1, '*', i, '=', num1 * i)





#56723 => o/p 32765
#approach => '56723' => '32765' => 32765
#approach 2 => 
#Q = 5672, R = 3
#Q = 567, R = 2 => 32
#Q = 56, R = 7 => 327
#Q = 5, R = 6 => 327* 10 + 6 = 3276
#Q = 0, R = 5 => 32760 + 5 => 32765


num12 = 12321
digit_sum = 0
rev_num = 0
count = 0

num1 = num12


while num1 != 0:
    rem = num1 % 10 #3 #2 #7 #6 #5
    digit_sum += rem
    rev_num = rev_num * 10 + rem #3 #32 #327 #3276 #32765
    num1 = num1 // 10 #5672 #567 #56 #5 #0
    count += 1

print(rev_num) #12321
print(digit_sum)
print(count)

#You should never tamper with the inputs

if rev_num == num12:
    print("Palindrome")
else:
    print("Not a palindrome")





#
db_username = 'Babu'
db_password = 'yam'


total_rem_chances = 3
while total_rem_chances > 0:
    input_username = input("Enter a username")
    input_password = input("Enter password")

    if input_username == db_username and input_password == db_password:
        print("Login succesful")
        break
        #total_rem_chances = 0
    else:
        total_rem_chances -= 1
        print("Invalid creds")
        print("You still have", total_rem_chances, "chances")
