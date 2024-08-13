first = 34
second = 46
third = 12
print(first)
print(second)
print(third)



if first == second and second == third and third == first:
    print('3')
elif first <= second and second >= third and third >= first:
    print("2")
elif first != second and second != third and third != first:
    print("0")


