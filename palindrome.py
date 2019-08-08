number1=int(input())
reverse=0
temp=0
temp=number1
if (temp>0):
    temp1=temp1%10
    reverse=reverse*10+temp1
    number1=number1//10
if (temp=reverse):
    print("yes")
else:
    print("no")
