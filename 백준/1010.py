# 백준 1010번 문제
# 다리놓기

# 강을 사이에 두고 서쪽에 N개, 동쪽에 M개의 사이트가 존재할 때(0<N<=M<=30)
# 다리를 겹치지 않게 사이트를 연결할 수 있는 경우의 수
# 겹치지 않게 하기 위해서는 다리가 연결됐을 때, 동쪽에서 보면
# 연결된 서쪽 사이트의 순서를 알 수 있다는 점이다.
# 따라서 동쪽의 M개의 사이트 중에서 N개를 고르면 되는 조합문제이다.


factorial = [1]*31
for i in range(2, 31):
    factorial[i] = i * factorial[i-1]
    
def combination(a, b):
    return factorial[a]//(factorial[b]*factorial[a-b])

t = int(input())
case = []

for _ in range(t):
    case.append(list(map(int, input().split())))
    
for c in case:
    print(combination(c[1], c[0]))