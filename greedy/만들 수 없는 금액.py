n = int(input())
data = list(map(int, input().split()))
data.sort()

# 타겟은 만들고자 하는 금액 1부터 올려가는 방식으로 계산
target = 1

# 현재 가지고 있는 동전 중에서 작은 동전부터 시작
# 타겟(만들고자 하는 금액) 보다 작거나 같은 동전이 없다면 해당 금액을 만들 수가 없음
# 아직 사용하지 않은 동전 중 타겟보다 작은 동전이 있다면 타겟의 범위는 그 동전만큼 증가
# 예를 들어 현재 타겟이 5라면 1부터 4까지는 만들어 낼 수 있음
# 다음 동전이 4라면 1~4 + 4 까지 만들 수 있기 때문에 1~8까지 만들 수 있음
# 따라서 타겟은 9로 증가(기존 타겟 5 + 다음 동전 4 = 새로운 타겟 9)

for x in data:
    if x > target:
        break
    target += x

print(target)
