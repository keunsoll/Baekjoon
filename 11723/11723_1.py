import sys

s = set()


def add(x):
    if x not in s:
        s.add(x)


def remove(x):
    if x in s:
        s.remove(x)


def check(x):
    if x in s:
        print(1)
    else:
        print(0)


def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)


def all():

    s = set([i for i in range(1, 21)])
    return s


def empty():

    s = set()
    return s


input = sys.stdin.readline
m = int(input())


for i in range(m):
    data = input().split()
    if len(data) == 1:
        if data[0] == 'all':
            s = all()

        else:
            s = empty()

    else:
        x = int(data[1])
        if data[0] == 'add':
            add(x)
        elif data[0] == 'remove':
            remove(x)
        elif data[0] == 'check':
            check(x)
        elif data[0] == 'toggle':
            toggle(x)
