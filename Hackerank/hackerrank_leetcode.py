# Solve Me First (HackerRank)
Program to add two numbers.
def solveMeFirst(a, b):
    return a + b
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)

Example
Input
2
3
Output
5

# Simple Array Sum (HackerRank)

def simpleArraySum(ar):
    return sum(ar)

n = int(input())
ar = list(map(int, input().split()))

result = simpleArraySum(ar)
print(result)

Example
Input

5
1 2 3 4 5

Output

15


#leetcode

# Say "Hello, World!" in Python
print("Hello, World!")

Output

Hello, World!

#Python If–Else (Weird / Not Weird)
n = int(input())

if n % 2 != 0:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
else:
    print("Not Weird")



# Arithmetic Operators
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

Output shows:

Addition

Subtraction

Multiplication

#Python Division
a = int(input())
b = int(input())

print(a // b)   # Integer division
print(a / b)    # Float division

Example
Input: 4 , 3

Output

1
1.3333333333

#Loops (Print Squares)
n = int(input())

for i in range(n):
    print(i ** 2)

Example
Input

5

Output

0
1
4
9
16


