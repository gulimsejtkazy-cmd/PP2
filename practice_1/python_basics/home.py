count = 1
where = input ("go left or right?")
while where == "right" and count != 2:
    where = input ("go left or right?")
    count+=1
    if(count==2):
        print("sad face")
    else:
        print("You got out!")