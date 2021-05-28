#Task1 
total = 0

for i in range(5):
    num = float(input('Enter Numbers: '))
    total += num
avg = total/5
print("Avg. of numbers is: ", avg)
#Task 2
N = int(input("Enter number: "))
if(N%2)==0:
    print('It is even')
else:
    print('It is Odd')
#Task 3
year = int(input('Enter Year : '))
if (year%4 == 0 and year % 100 != 0 or year%400 == 0):
    print("It is a leap year", year)
else:
    print("It is not a leap year", year)
#Task 4
Num =  float(input('Enter a Number: '))
if num > 0:
    print('It is Positive')
elif num == 0:
    print('Zero')
else:
    print('It is Negative')
#Task 5
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
if (num1>num2):
    print('{} is larger'.format(num1))
elif(num2>num1):
    print('{} is larger'.format(num2))
else:
    print('{} and {} are equal'.format(num1,num2))
#Task 6
num = int(input('Enter a number :'))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print("The factorial of num is : ",end="")
print(factorial)
#Task 7
x = int(input('Enter First number: '))
y = int(input('Enet Second number: '))
temp = x
x = y
y = temp

print('Value of x is ',x)
print('Value of y is ',y)

#Task 8
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
if (num1>num2):
    print('{} is smaller'.format(num2))
elif(num2>num1):
    print('{} is smaller'.format(num1))
else:
    print('{} and {} are equal'.format(num1,num2))

#Task 9
num = int(input("Enter a number: "))
if (num<100 and num%2 == 0 ):
    print('Even')
elif(num>100):
    print('The number is greater than 100')
else:
    print('Odd')

#Task 10
Num = int(input('Enter a Number: '))
if (Num<10):
    print(Num*Num)
else:
    print('Number is greater than 10')
#Task 11
num = float(input('Enter a number: '))
if num >= 0:
    if num == 0:
        print('The number is Zero')
    else:
        print('The number is positive')
else:
    print('The Number is Negative.')
#Task 12
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
if a>b:
    if a>c:
        print('a is largest')
    else:
        print('c is largest')
else:
    if b>c:
        print('b is largest')
    else:
        print('c is largest')
#Task 13
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
if(a<=b and a<=c):
    print("a is smallest")
elif(b<=a and b<=c):
    print("b is smallest")
else:
    print("c is smallest")
#Task 14
x = int(input('Enter a number: '))
y = int (input('Enter a number: '))
print('Befor swap')
print("x is",x, "and y is",y )
x,y = y,x
print('After Swap')
print("x is",x, "and y is",y )
#Task 15
x = int(input('Enter starting number: '))
y = int(input('Enter ending number: '))
for i in (range(x,y-1,-3)):
    print(i)