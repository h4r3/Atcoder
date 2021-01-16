a,b=map(str, input().split())
if (int(a+b))**(0.5)%1==0:
    print("Yes")
else:
    print("No")