def cal1(x):
    return 5*x


def cal2(x):
    return 3*x


def cal3(x):
    return 2*x


def cal4(x):
    return 1+x


x = int(input())
INF = 123456789
d = [INF] * (5*x+1)
d[1] = 0
dCal = [cal1, cal2, cal3, cal4]

for i in range(1, x+1):
    # *5, *3, *2, +1
    nd = d[i]+1
    for cal in dCal:
        ni = cal(i)
        if ni > x:
            continue
        if d[ni] > nd:
            d[ni] = nd

print(d[x])
