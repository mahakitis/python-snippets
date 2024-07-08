a = 1234
rev = 0

rem = a%10
rev = rev*10+rem
a //= 10

rem = a%10
rev = rev*10+rem
a //= 10

rem = a%10
rev = rev*10+rem
a //= 10

rem = a%10
rev = rev*10+rem
a //= 10

print("reverse of number  - ",rev)