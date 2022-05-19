# # Input an integer,and print the multiplication table for the number.
# num = int(input("Enter the number:"))
# print("Multiplication Table of ", num)
# for i in range(1, 11):
#     print(num, 'x', i, '=', num*i)

# # Input 10 characters using while loop and count how many vowels are there.
# str = input("Please enter a string as you wish:")
# vowels = 0
# for i in str:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
#        i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#         vowels += 1


# print("The number of vowels:", vowels)

# # Find sum of numbers from 1 to 100 which are divisible by either 2 or 3
# n = []
# for x in range(1, 100):
#     if(x % 2 == 0 or x % 3 == 0):
#         n.append(x)
# print(sum(n))

# Input a float number which will be the side of square,prompt user to enter a positive value if user inputs a negative value.Finally calculate the area of the square.

n1 = float(input("enter the number"))

for i in range(1):
    if(n1 < 0):
        continue
    else:
        print(n1*n1)
