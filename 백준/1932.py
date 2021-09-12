# 백준 1932번 문제
# 정수 삼각형 (동적 계획법)

# 숫자로 이루어진 삼각형을 꼭대기부터 내려오며 수를 더한다.
# 경로를 거친 숫자들의 총합이 최대가 되도록 계산한다.
# 피라미드를 가장 아래서부터 시작하여 한단계씩 위로 올라가며 해당 경로로 가는 최댓값을 구한다.
n = int(input())
pyramid = []

for _ in range(n):
    pyramid.append(list(map(int, input().split())))
    
pyramid.reverse()
cost = pyramid[0]

for line in pyramid[1:]:
    tempCost = [0] * len(line)
    for i in range(len(line)):
        tempCost[i] = max(cost[i],cost[i+1]) + line[i]
    cost = tempCost
        
print(cost[0])