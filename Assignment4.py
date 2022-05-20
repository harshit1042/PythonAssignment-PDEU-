# 1. Take a single input from  user and return its integer value.
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

# 2.Print the results of the  arithmetic operations


def arith(a, b):
    sum = a+b
    print('Adding {0} with {1}: {2}'.format(a, b, sum))
    sub = a-b
    print('Substract {1} with {0}: {2}'.format(a, b, sub))
    multi = a*b
    print('multiply {0} with {1}: {2}'.format(a, b, multi))
    div = a/b
    if(b != 0):
        print('divide {0} with {1}: {2}'.format(a, b, div))
    else:
        print("Not defined")


a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print(arith(a, b))
