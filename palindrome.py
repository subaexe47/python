number1=int(input())
reverse=0
temp=0
temp=number1
if (temp>0):
    temp=temp%10
    reverse=reverse*10+temp
    number1=number1//10
if (temp==reverse):
    print("yes")
else:
    print("no")
