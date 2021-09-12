# 백준 12856번 문제
# 평범한 배낭

# 무게제한의 최댓값을 1~k 까지 두고
# 물건의 개수를 하나씩 늘려가며 테이블을 작성하듯 
# 해당 무게제한에서 현재 물건을 가지고 만들 수 있는 가치의 최댓값을 구한다.

import sys

n,k = map(int, sys.stdin.readline().strip().split())

weight = [0]
value = [0]

for _ in range(n):
    w, v = map(int, sys.stdin.readline().strip().split())
    weight.append(w)
    value.append(v)
    
sumValue = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < weight[i]:
            sumValue[i][j] = sumValue[i-1][j]
        else:
            sumValue[i][j] = max(sumValue[i-1][j-weight[i]] + value[i], sumValue[i-1][j])

print(sumValue[-1][-1])

#     0   6   4   3   5
# 1   0   0   0   0   0
# 2   0   0   0   0   0
# 3   0   0   0   6   6
# 4   0   0   8   8   8
# 5   0   0   8   8   12
# 6   0   13  13  13  13
# 7   0   13  13  14  14