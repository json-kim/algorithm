# 백준 2580번 문제
# 동전 0

# 동전의 개수 n, 가치의 합 k
n, k = map(int, input().split())
minimum = 0
coins = []

for _ in range(n):
    coins.append(int(input()))
    
for i in range(n-1, -1, -1):
    coin = coins[i]
    if k >= coin:
        minimum = minimum + k // coin
        k = k % coin
    if k == 0:
        break
    
print(minimum)