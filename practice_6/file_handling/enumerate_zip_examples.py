# 1
names = ["Ali", "Aruzhan", "Dias"]

# enumerate
for i, name in enumerate(names):
    print(i, name)

# zip
ages = [20, 21, 19]
combined = list(zip(names, ages))
print(combined)

# 2
names = ["Ali", "Aruzhan", "Dias"]
ages = [20, 21, 19]

for i, name in enumerate(names):
    print(i, name)

print(list(zip(names, ages)))