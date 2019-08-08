prime=int(input())
count = 0
for i in range (1,prime+1):
    if((prime%i)==0):
        count=count+1
if(count==2):
    print("yes")
else:
    print("no")
