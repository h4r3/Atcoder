#4 inputでない
n=963761198400
cnt=0
for first in range(-n,n+1,1):
    sum=0  
    for i in range(first,n+1,1):
        
        if sum==12:
            
            print(sum)
            cnt+=1
            break
        sum+=i
if n==1:
    print(2)  
else:
    print(cnt*2)
        


"""
N,M=map(int, input().split())
SUM=0
lists1=[]
lists2=[]
for cnt in range(M):
    A,B=map(int, input().split())
    list1=[A,B]
    lists1.append(list1)
K=int(input())
for cnt2 in range(K):
    C,D=map(int, input().split())  
    list2=[C,D]
    lists2.append(list2)
#print(lists1)
#print(lists2)
for l1 in range(len(lists1)):
    try:
        SUM+=lists2.count(lists1[l1])
    except:
        pass
print(SUM)

"""




"""以上と以下で３ミス
#A,B,C=map(int, input().split())
N,S,D=map(int, input().split())
ATK=0
for cnt in range(N):
    X,Y=map(int, input().split())
    if X>=S or Y<=D:
        pass
    elif X<S and Y>D:
        ATK=1

if ATK==1:
    print("Yes")
elif ATK==0:
    print("No")
"""


"""A
A,B,C=map(int, input().split())
if C==0 and A>B:
    print("Takahashi")
elif C==0 and A<=B:
    print("Aoki")
elif C==0 and A<=B:
    print("Aoki")
elif C==1 and A<B:
    print("Aoki")
elif C==1 and A>=B:
    print("Takahashi")

"""