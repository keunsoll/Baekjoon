import sys
input = sys.stdin.readline
n, m = map(int, input().split())
t = list(map(int, input().split()))
start = 0
end = max(t)

while start <= end:
    mid = (start+end)//2
    tree = 0
    for i in t:
        if i > mid:
            tree += i-mid
    if tree >= m:
        start = mid+1
    else:
        end = mid-1
print(end)
