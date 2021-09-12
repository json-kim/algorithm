# 백준 9375번 문제
# 패션왕 신해빈

# 의상과 의상의 종류가 주어진다.
# 종류별로 하나의 의상만 입을 수 있다.
# 가능한 의상의 조합을 구하기.(해당 종류의 의상을 입지 않는 것도 가능하다.)
# 단 아예 벗는 경우는 제외(-1)

t = int(input())
case = []

for i in range(t):
    n = int(input())
    wear = {}
    
    for j in range(n):
        cloth, category = map(str, input().split())
        if wear.__contains__(category):
            wear[category].append(cloth)
        else:
            wear[category] = [cloth]
    
    case.append(wear)
    
for c in case:
    result = 1
    for val in c.values():
        result = result * (len(val)+1)
    
    print(result-1)
    