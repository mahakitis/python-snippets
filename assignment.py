#Q.1 Write a program accepts two numbers from user and calculates first no is divisible by second or not.
#a = int(input("value of a - "))
#print("a = ",a)
#b = int(input("value of b - "))
#print("b = ",b)
#if a/b==0 :
#   print("numbers are divisible ")
#else :
#    print("numbers are not divisible ")

#Q.2 Write a program accepts a number from user and check given number is even or odd.
#a = int(input("value of a - "))
#print("a = ",a)
#if a%2==0 :
#    print("number is even ")
#else :
#    print("numbers is odd")

#Q.3 Write a program accepts two numbers from user and calculate biggest number out of two numbers.
#a = int(input("value of a - "))
#print("a = ",a)
#b = int(input("value of b - "))
#print("b = ",b)
#if a>b:
#    print("a is greatest ")
#else :
#    print("b is greatest ")

#Q.4 Write a program accepts three numbers from user and calculate biggest number out of three numbers.
#a = int(input("value of a - "))
#print("a = ",a)
#b = int(input("value of b - "))
#print("b = ",b)
#c = int(input("value of c - "))
#print("c = ",c)
#if a>b and a>c :
#    print("a is greatest")
#elif b>c :
#    print("b is greatest")
#else :
#    print("c is greatest")

#Q.5 Write a program accepts a number from user and check given number is palindrome number or not.(for 3 didgit)
# a = int(input("value of a - "))
# print("a - ",a)
# num1=a
# rev=0
# num=num1%10
# rev=rev*10+num
# num1//=10

# num=num1%10
# rev=rev*10+num
# num1//=10

# num=num1%10
# rev=rev*10+num
# num1//=10

# if a==rev:
#     print("a is palindrome")
# else:
#     print("a is not palindrome")

#Q.6 Write a program accepts a number from user and check given number is Armstrong number or not.(for 3 digit)
# a = int(input("value of a - "))
# print("a - ",a)
# num1=a
# sum=0
# num=num1%10
# sum=sum*10+num**3
# num1//=10

# num=num1%10
# sum=sum*10+num**3
# num1//=10

# num=num1%10
# sum=sum*10+num**3
# num1//=10

# if a==sum:
#     print("a is an armstrong number")
# else:
#     print("a is not an armstrong number")

#Q.7 Write a program accept a three digits number from user and check biggest digit of given number.

#Q.8 Write a program that accepts a number from user and calculate whether it is positive or negative or zero
# a=int(input("value of a - "))
# print("a -",a)
# if a>0:
#     print("a is positive number")
# elif a==0:
#     print("a is zero")
# else:
#     print("a is negative number")

#Q.9 Write a program to calculate whether character is in lowercase or uppercase.
# a=input("value - ")
# print("a - ",a)
# if a>="A" and a<="Z":
#     print("given character is in uppercase")
# else:
#     print("given character is in lowercase")

#Q.10 Write a program to calculate whether a character is vowel or consonant.
# char=input("value - ")
# print("a - ",char)
# vowel = "a","e","i","o","u","A","E","I","O","U"
# if char in vowel:
#     print("given character is a vowel")
# else:
#     print("given character is a consonant")

# Q.11 Write a program that accepts five subjects’ marks from user and calculate the total marks then
# calculate
# Percentage Display message according to following condition.
# Percentage >=60 then print message Grade A
# Percentage >=50 then print message Grade B
# Percentage >= 40 then print message Grade C
# Percentage < 40 then print message Grade D

# sub1=int(input("marks for sub1"))
# sub2=int(input("marks for sub2"))
# sub3=int(input("marks for sub3"))
# sub4=int(input("marks for sub4"))
# sub5=int(input("marks for sub5"))
# print("marks are - ",sub1,sub2,sub3,sub4,sub5)
# sum=sub1+sub2+sub3+sub4+sub5
# if sum>=60:
#     print("grade a")
# elif sum>=50:
#     print("grade b")
# elif sum>=40:
#     print("grade c")
# else:
#     print("grade d")


# Q.12 Write a program for generating electricity Bill Accept last month unit and current month unit from
#  user, then calculate and print bill amount according to following condition
#  0-150 charges 4 rs/unit , 151-300 charges 6 rs/unit , 301-500 8rs/unit , >500 charges 10rs/unit

# current_unit = int(input("current month unit - "))
# print("unit used in current month - ",current_unit)
# last_unit = int(input("last month unit - "))
# print("unit used in last month ",last_unit)
# units = current_unit-last_unit
# if units<=150:
#     print("total bill generated ",units*4)
# elif units>=151 and units<=300:
#     print("total bill generated ",units*6)
# elif units>=301 and units<=500:
#     print("total bill generated ",units*8)
# else:
#     print("total bill generated ",units*10)


#  Q.13 Write a program to accept basic salary from user, if basic salary is between 0 and 15000 then TA is
#  8% of basic salary, DA is 4% of basic salary. If salary is above 15000 then TA is 10% of basic salary, DA is
#  5% of basic. Calculate gross salary as gs=basic salary+TA+DA?

basic_salary=int(input("basic salary - "))
print("basic salary is ",basic_salary)
if basic_salary<=15000:
    ta = 0.8*basic_salary
    da = 0.4*basic_salary
    gross_salary=ta+da+basic_salary
    print("the total gross salary is ",gross_salary)
else:
    ta = 0.1*basic_salary
    da = 0.5*basic_salary
    gross_salary=ta+da+basic_salary
    print("the total gross salary is ",gross_salary)