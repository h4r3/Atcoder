#a,b=map(str, input().split())
N=int(input())
for i in range(N):
    t,x,y=map(int, input().split())
    if ((t/(x+y))%2)==1:
        c=1
    else:
        c=0
if c==1:
    print("Yes")
else:
    print("No")

    #if (t%2**N)//(x+y)!=0:
#   print("No")