# To handle zero divison error
try:
from math import sqrt
num1 = int(input(" enter any number "))
num2 = int(input("enter any number "))
res = num1/num2
print(res)
except:
    print("Exception Caught ZERO DIVISION ERROR")


# To handle error while working with file
filename = input("Enter the file name")
try:
    f_obj = open(filename)
    content = f_obj.read()
except FileNotFoundError:
    msg = "The file " + filename + " does not exist."
    print(msg)
else:
    print(content)
    f_obj.close()


# To handle value error
num = int(input("Enter a integer:"))
try:
    print(sqrt(num))
except:
    print("Entered incorrect value")
