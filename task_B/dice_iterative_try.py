import random
surface = input("サイコロの面の数は?:")
count = input("何回振りますか?:")

result = []
for challenge in range(int(count)):
    value = random.randint(1, int(surface))
    result.append(value)
print(result)