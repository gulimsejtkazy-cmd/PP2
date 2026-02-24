# 1
year=int(input())
month=int(input())
day=int(input())
if day<31:
    if month==1 and day<5:
        month=12
        day=(day+31)-5
        year-=1
    elif(day<5):
        if month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            month-=1
            day=(day+31)-5
        elif(month==4 or month==6 or month==9 or month==11):
            month-=1
            day=(day+30)-5
        elif(month==2):
            month-=1
        if(day==28):
            day=(day+28)-5
        else:
            day=(day+29)-5
    else:
        day=day-5
    print(f"{year}-{month}-{day}")
else:
    print("Invalid date")
# 2
# 3
# 4
