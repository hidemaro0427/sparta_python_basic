even_numbers = [2, 4, 6, 8]

for number in even_numbers:
    print(number * 2)

assert isinstance(even_numbers, list)
assert isinstance(even_numbers[0], int)
assert len(even_numbers) == 4
assert len(even_numbers) != 10
