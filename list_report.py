# Part C - List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# Numbered list
number = 1
for item in items:
    print(f"{number}. {item}")
    number += 1

# Count names with more than 4 letters
count = 0
for item in items:
    if len(item) > 4:
        count += 1
print("Items with more than 4 letters:", count)

# Longest item name (loop comparison)
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item
print("Longest item name:", longest)