n, m = map(int, input().split())
ball = list(map(int, input().split()))
arr = [0] * (n+1)

for x in ball:
    arr[x] += 1

count = 0

for i in range(1, m+1):
    n -= arr[i]
    count += arr[i] * n

print(count)
