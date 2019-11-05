
line_input = int(input("行数を入力してください:"))
column_input = int(input("列数を入力してください:"))

for line in range(1, line_input + 1):
    for column in range(1, column_input +1):
        print(column * line, end="")
    print()