# 1
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
# 2
with open("sample.txt", "r") as f:
    print(f.read())
