"""
a=int(input())
b,c=int(input()),int(input())
s=str(input())
print(a+b+c," "+s+"/n")
"""

##Ans
#ref https://qiita.com/863/items/b970d2f376c1e16c921b
a = int(input())
b, c =(int(x) for x in input().split())
#or map関数　第一引数に関数、第二引数にシーケンス
#b, c = map(int, input().split())
print(a+b+c, input())