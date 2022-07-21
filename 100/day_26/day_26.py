numbers = [1, 2, 3, 4]
new_numbers = [n + 1 for n in numbers]

print(new_numbers)

doubled = [num * 2 for num in range(1, 5)]
print(doubled)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

upper_names = [name.upper() for name in names if len(name) > 5]

print(upper_names)