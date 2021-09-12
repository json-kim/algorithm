# 백준 1149번 문제
# RGB거리 (동적 계획법)

# 1번부터 n번째까지 집이 순서대로 있을 때, 인접한 집을 같은 색으로 칠하지 않으면서
# 최소 비용을 사용하도록 계산
# 고려해야할 것은 현재 집의 색상을 선택했을 때 각각의 최솟값들을 계산
# 첫번째 최소비용은 첫번째 집의 RGB 비용
# 한 집 씩 이동하며 그 집에서 RGB 최솟값을 이전 집까지의 최솟값들과 비교하며 계산
n = int(input())
RGBs = []
RGB = [0,1,2]

for _ in range(n):
    RGBs.append(list(map(int, input().split())))
    
cost = RGBs[0]

for rgb in RGBs[1:]:
    r = rgb[0] + min(cost[1], cost[2])
    g = rgb[1] + min(cost[0], cost[2])
    b = rgb[2] + min(cost[0], cost[1])
    cost = [r, g, b]
    
print(min(cost))
        
