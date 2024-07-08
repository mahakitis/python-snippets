                             #WHILE LOOP
# Q.1 Write a program to find out reverse of a given number.
# a=int(input("insert a number - "))
# rev=0
# while a!=0:
#     rem = a%10
#     rev = rev*10+rem
#     a //= 10

# print("reverse of the given number is - ",rev)

# Q.2 Write a program that accepts a number from user and check given number is palindrome number or not.
# a = int(input("value of a - "))
# num1 = a
# rev= 0
# while a>0:
#    num = a % 10
#    rev = rev* 10 + num
#    a //= 10

# if num1 == rev:
#     print("given number is Palindrome number")
# else:
#     print("given number is not a Palindrome number")

# Q.3 Write a program that accepts a number from user and check given number is Armstrong number or not.
# a=int(input("Enter the number:\n"))
# n=a
# final=n
# count=0 
# while a != 0:
#     a //= 10
#     count += 1 
# print("Number of digits by user: ", count)
# sum=0
# while n>0:
#     r=n%10 
#     sum = sum + (r**count) 
#     print(r,"power of",count,"=",(r**count))
#     n//=10
# print(sum)
# if sum==final:
#     print(final,"is an Armstrong Number")
# else:
#     print(final,"is not an Armstrong Number")

# Q.4 Write a program to print Fibonacci Series.
# num = int(input("Enter the Number Range: "))
# n1 = 0
# n2 = 1
# i = 0
# while i < num:
#     print(n1, end = '  ')
#     Next = n1 + n2
#     n1 = n2
#     n2 = Next
#     i = i + 1
    
# Q.5 Write a program to calculate sum of digits of a number.
# a=int(input("insert a number"))
# sum=0
# while a>0:
#     num = a%10
#     sum = sum+num
#     a //= 10
# print("the sum is - ",sum)

# Q.6 Write a program to calculate sum of squares of n natural number.
# num=int(input("insert a value for sum of n natural num"))
# sum=0
# while num>0: 
#     sum=sum+num**2
#     num -= 1
# print("the sum of given number square is - ",sum) 

# Q.7 Write a program to accept n number from user and show how many number are even or odd.
# num = int(input("insert a number"))
# a = 1
# ecount = 0
# ocount = 0
# while a <= num:
#     if a % 2 == 0:
#         ecount += 1
#     else:
#         ocount += 1
#     a += 1 

# print("Odd Number :", ocount)
# print("Even Number :", ecount)

# Q.8 Write a program to find LCM of two numbers.
# n1=int(input("insert num1 - "))
# n2=int(input("insert num2 - "))
# print("numbers are - ",n1,n2)
# max=0
# if n1>n2:
#     max=n1
# else:
#     max=n2

# while 1:
#     if max%n1==0 and max%n2==0:
#        print("L.C.M is:",max)
#        break
#     max+=1

# Q.9 Write a program to find HCF of two numbers.
# n1=int(input("insert num1 - "))
# n2=int(input("insert num2 - "))
# print("numbers are - ",n1,n2)
# count=1
# hcf=0
# while count<= n1 and count<=n2:
#     if n1%count == 0 and n2%count == 0:
#         hcf = count 
#     count+=1
# print("HCF is ",hcf)
    
# Q.10 Write a program that accepts a number from user and check given number is prime number or not.
# a = int(input("Enter the number:\n"))  
# n = 0
# i = 2
# while i < a:
#     if a % i == 0:
#         n=1
#         break
#     i+=1   
# if n==0:
#     print(" given number is prime number")
# else:
#     print("given number is not a prime number")