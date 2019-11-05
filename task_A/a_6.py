odd_numbers = [1, 3, 5, 7, 9]

count = 0
for number in odd_numbers:
    print(odd_numbers[count])
    count += 1

assert isinstance(odd_numbers, list)
assert isinstance(odd_numbers[0], int)
assert isinstance(odd_numbers[3], int)
assert len(odd_numbers) == 5