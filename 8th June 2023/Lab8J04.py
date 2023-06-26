# Identity Operators (is, is not)
a = 5 # Values are checked
b = 5
print(a is b)

password = "pramod"
confirm_password = "pramod"
print(password is confirm_password)
print(id(password))
print(id(confirm_password))



list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1[1] is list2[0])