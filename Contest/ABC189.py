
"""
#C
from itertools import groupby

_n=6#int(input())
_A=list(map(int, input().split()))
ans=0
minA=min(_A)
maxA=max(_A)
cntA=len(_A)
#for k, g in groupby(enumerate(data), lambda (i, x): i-x):
for xx in range(minA,maxA+1,1):
    cntx = [sum(1 for ii in num) for _, num in groupby(_A, lambda x: x >= xx)]
    r_l=max(cntx)
    current=xx*r_l
    #print(xx,cntx)
    if current>ans:
        ans=current
print(ans)
"""

_A=[2,4,4,9,4,9]

A=(_A, lambda x: x >= xx)
   
"""
#B WA 7/28  1浮動小数点による誤判定
#しかし、浮動小数点数の演算は一般に誤差を含みます。
# 例えば、以下の入力の正しい答えは -1 ですが、
# 実装と環境によっては 3 を出力する場合があります。
#3 13
#30 13
#35 13
#35 13
#整数のみで計算できるように適切な式変形を行う

_n,_x=map(int, input().split())
_sum=0
for cnt in range(_n):
    _v,_p=map(int, input().split())
    _sum += _v*_p       #1 _sum += _v*_p/100
    if _sum>_x*100:     #1 if _sum>_x: 
        print(cnt+1)
        exit() #ループを抜け出すbreakだと誤検知されるよう
print(-1)


#A CA
slot=input()
C1,C2,C3=slot[0],slot[1],slot[2]
if C1==C2 and C1==C3:print("Won")
else:print("Lost")
"""