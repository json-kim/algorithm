# 백준 2156번 문제
# 포도주 시식 (동적 계획법)

# 포도주 잔을 선택하면 다 마신다.
# 연속으로 놓여있는 3잔을 모두 마실 수는 없다.
# 가장 많은 양의 포도주를 마실수 있도록 계산하고 최댓값 구하기
# n번째 잔이 놓여있을 때의 최댓값은 n-1번째 최댓값에서 n번째 잔을 더 마시거나(마실수 있다면), n-2번째 최댓값에서 n번째 잔을 마시거나,
# n번째 잔을 마시지 않고 n-1번째 까지 마실때까지중 최댓값이다.

n = int(input())
wine = [0]

for _ in range(n):
    wine.append(int(input()))

drink = [0] * (n+1)
drink[1] = wine[1]
if n>1:
    drink[2] = wine[1] + wine[2]
if n>2:
    drink[3] = max(drink[0] + wine[2] + wine[3], drink[1] + wine[3], drink[2])

for i in range(4, n+1):
    drink[i] = max(drink[i-3] + wine[i-1] + wine[i], drink[i-2] + wine[i], drink[i-1])
    
print(drink[n])