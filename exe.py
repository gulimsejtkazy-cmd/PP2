import datetime
a = input().split("-")
b = input().split("-")

c = datetime.date(int(a[0]), int(a[1]), int(a[2]))
d = datetime.date(int(b[0]), int(b[1]), int(b[2]))

s = c - d

print(abs(s.total_seconds()))