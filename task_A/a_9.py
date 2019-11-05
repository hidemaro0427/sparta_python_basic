kazuma_info = {"first_name":"Kazuma",
               "family_name":"Takahashi",
               "age":35}

print(kazuma_info["first_name"])
print(kazuma_info["family_name"])
print(kazuma_info["age"])

assert isinstance(kazuma_info, dict)
assert isinstance(kazuma_info["first_name"], str)
assert isinstance(kazuma_info["age"], int)
