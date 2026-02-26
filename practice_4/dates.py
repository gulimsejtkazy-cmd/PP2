# 1
import datetime
today=datetime.date.today()
x=today-datetime.timedelta(days=5)#timedelta = interval used to add or subtract time
print(x)

# 2
import datetime
today=datetime.date.today()
yesterday=today- datetime.timedelta(days=1)
tommorrow=today+ datetime.timedelta(days=1)
print(f"yesterday-{yesterday},today-{today},tomorrow-{tommorrow}")

#  3
import datetime

now = datetime.datetime.now()

new_time = now.replace(microsecond=0)

print(new_time)
# 4
import datetime
d1 = datetime.date(2026, 2, 25)
d2 = datetime.date(2026, 2, 24)

diff = d1 - d2
print(diff.total_seconds()) 
