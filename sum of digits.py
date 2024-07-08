a = 123
sum = 0

num = a%10
sum = sum+num
a //= 10

num = a%10
sum = sum+num
a //= 10

num = a%10
sum = sum+num
a //= 10


print("sum of digits - ",  sum)