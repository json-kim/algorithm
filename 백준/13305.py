# 백준 13305번 문제
# 주유소 (그리드)

# 첫 도시에서는 무조건 기름을 충전해야 한다.
# 오른쪽으로 한칸씩 이동하며 비용(거리 * 최소가격)을 더해간다.
# 이동한 도시의 가격이 더 낮을 경우 최소가격을 갱신하고 다음 계산부터 적용한다.

# 도시의 개수
n = int(input())
# 도시 사이의 거리
distance = list(map(int, input().split()))
# 각 도시의 주유소 가격
price = list(map(int, input().split()))

min_cost = price[0]
cost = distance[0] * min_cost
current = 1

# 가장 가격이 싼 도시를 찾는 과정을 반복
while current < n-1:
    
    # 다음 도시가 기름값이 더 싼 경우
    if min_cost > price[current]:
        min_cost = price[current]
        cost = cost + min_cost * distance[current]
    else:
        cost = cost + min_cost * distance[current]
    
    current = current + 1
        
print(cost)