user_input1 = int(input("Enter the first number\n"))
user_input2 = int(input("Enter the second number\n"))

def minimum(first, second):
    if (first < second):
        return first
    else:
        return  second


#return ?
min_n0 = minimum (user_input1, user_input2)
print("Min is - > "+ str(min_n0))