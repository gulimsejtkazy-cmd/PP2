from datetime import date
d1 = date(2026, 2, 25)
d2 = date(2026, 2, 24)

diff = d1 - d2
print(diff.total_seconds()) 