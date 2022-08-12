import math
import sys

input=sys.stdin.readline
a,b,v=map(int,input().split())
ans=(v-b)/(a-b)
print(math.ceil(ans)) # ceil(): 올림 내장 함수