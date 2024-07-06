my_dict = { 'Tamara' : 1989, 'Stefaniia': 2020, 'Max': 1987, 'Roman': 1980}
print(my_dict)
print(my_dict.get('Max'))
print(my_dict.get('Alex', 'Выберите другое имя'))
my_dict.update ({'Igor': 1968, 'Irina': 1988})
del my_dict['Max']
print(my_dict)

my_set = {12, 11, 23, 12,23,23,11,5}
print(my_set)
my_set.add(1)
my_set.add(7)
my_set.remove(12)
print(my_set)

