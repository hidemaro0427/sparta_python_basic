def sum_value(numbers):
    total = numbers[0]
    for number in numbers:
        total += number
    return total

def maximum(numbers):
    max = 0
    for number in numbers:
        if max < number:
            max = number
    return max

numbers = input("データを入力してください(スペース区切り) >")
list = []
for number in numbers.split(" "):
    list.append(int(number))

print(sum_value(list))
print(maximum(list))
