# 백준 2579번 문제
# 계단 오르기 (동적 계획법)

# 계단은 한번에 한개 혹은 두개를 밟을 수 있다.
# 연속된 세개의 계단은 밟으면 안된다(시작점-바닥 제외)
# 마지막 계단은 밟아야 한다.
# 위의 규칙을 지키며 최대의 점수를 구해야 한다.
# n이 1일 때, 2일 때, 3일 때의 최대값은 기본값으로 구한다.
# n번째 계단에 올라갈 때, n-2계단에서 2칸을 올라가는 방법, n-1계단에서 1칸을 올라가는 방법이 있다.
# 단 연속된 3개의 계단을 밟으면 안되기 때문에, 직전계단에서 1칸을 올라가는 경우는 전전과정에서 2칸을 올라온 뒤 1칸을 올라가야만 한다.
# 따라서 n-2칸에서 2칸 올라온경우, n-3칸에서 2칸 올라오고 1칸 올라온 경우중 최댓값이 해당 계단을 올라오는 비용의 최댓값이 된다.
n = int(input())
stair = []

for _ in range(n):
    stair.append(int(input()))
    

cost = [stair[0]]
if n > 1:
    cost.append(max(cost[0]+stair[1], stair[1]))
if n > 2:
    cost.append(max(cost[0]+stair[2], stair[1]+stair[2]))

for i in range(3,n):
    cost.append(max(stair[i]+cost[i-2], cost[i-3]+stair[i-1]+stair[i]))

print(cost[-1])