d1 = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d1[x] != 0:
        return d1[x]
    d1[x] = fibo(x-1) + fibo(x-2)
    return d1[x]


print('재귀(탑다운):', fibo(99))

d2 = [0] * 100

d2[1] = 1
d2[2] = 1
n = 99

for i in range(3, n+1):
    d2[i] = d2[i-1] + d2[i-2]

print('반복문(보텀업):', d2[99])
