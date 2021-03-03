n, m = map(int, input().split())
arr = []
arr.sort()
d = [10001]*10001

for _ in range(n):
    input_data = int(input())
    arr.append(input_data)
    d[input_data] = 1

for i in range(1, m+1):
    for j in arr:
        if i - j < arr[0]:
            continue
        if d[i - j] != 10001:
            d[i] = min(d[i], d[i - j] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
