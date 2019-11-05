users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]

for user_info in users_info:
    print(f"Name: {user_info[0]} age: {user_info[1]}")

assert isinstance(users_info, list)
assert len(users_info) == 3
assert len(user_info) == 2
assert isinstance(user_info[0], str)
assert isinstance(user_info[1], int)
