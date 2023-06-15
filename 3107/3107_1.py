address = list(input().split(':'))

# 연속으로 : 있을 때
if "" in address:
    cnt = address.count("")
    length = len(address)-cnt

    index = address.index("")
    for i in range(8-length):
        address.insert(index+i, "0000")

    for _ in range(cnt):
        address.remove("")


for i in range(len(address)):
    if len(address[i]) != 4:
        address[i] = "0"*(4-len(address[i]))+address[i]

print(":".join(address))
