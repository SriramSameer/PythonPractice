def sum_of_three_number(a, b, c):
    d = a + b + c
    return d

result = sum_of_three_number(1, 2, 3)
print(result)


r = lambda x, y, z: x + y + z
r2 = lambda x, y, z, a: x + y + z + a
r3 = lambda a: pow(2, a)

print(r(3, 4, 5))
print(r(4, 5, 6))
print(r(4, 2, 1))
print(r(-1, -1, 2))