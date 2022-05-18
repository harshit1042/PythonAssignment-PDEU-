# Question 1
print("Q1:take two float as input and print all the permutations of the applicable operators on them.")
a = float(input("Enter first value "))
b = float(input("Enter second value "))
# 1. Addition (+)
print(a+b)

# 2. Subtraction (-)
print(a-b)

# 3. Multiplication (*)
print(a*b)

# 4. Division (/)
print(a/b)

# 5. Modulus(%)
print(a % b)

# 6. Exponentiation (**)
print(a**b)

# 7. Floor Division (//)
print(a//b)


# 2. Assignment Operators:

# "+=" Operator
a += b
print(a)

# '-=' Operator
a -= b
print(a)

# '*=' Operator
a *= b
print(a)

# '/=' Operator
a /= b
print(a)

# '%=' Operator
a %= b
print(a)

# '//=' Operator
a //= b
print(a)

# "**="
a **= b
print(a)
0.0
# 3. Comparison Operators:

# Equal (==) Operator
print(a == b)

# Not equal (!=) Operator
print(a != b)

# Greater than (>) Operator
print(a > b)

# Less than (<) Operator
print(a < b)

# Greater than or equal to (>=) Operator
print(a >= b)

# Less than or equal to (<=) Operator
print(a <= b)


# 4. Logical Operators:

# 'and' Operator :
print(a and b)
print(a < 3 and b < 5)

# 'or' Operator :
print(a or b)
print(a < 3 or b < 5)

# 'not' Operator:
print(not(a < 3 and b < 5))

# Question 2
print("Q2.Take 5 interger values as input and print the quotient and remainder when the maximum of them is divided by the minimum of them.")

lst = []

num = 5

for n in range(num):
    numbers = int(input('Enter number:'))
    lst.append(numbers)

q = max(lst)//min(lst)
print("Quotient is", q)
r = max(lst) % min(lst)
print("Remainder is", r)
