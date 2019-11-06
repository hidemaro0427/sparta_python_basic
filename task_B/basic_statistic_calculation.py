def sum_value(numbers):
    total = numbers[0]
    for number in numbers:
        total += number
    return total

numbers = input("データを入力してください(スペース区切り) >")
list = []
for number in numbers.split(" "):
    list.append(int(number))

print(sum_value(list))