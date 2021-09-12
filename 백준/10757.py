# 백준 10757번 문제
# 큰 수 A+B

A, B = map(str, input().split())
result = []

n = min(len(A), len(B))

up = 0
for i in range(1, n+1):
    plus = int(A[-i]) + int(B[-i]) + up
    up = plus // 10
    result.append(plus % 10)
    
bigger = A if len(A) >= len(B) else B

for i in range(n+1, len(bigger)+1):
    plus = int(bigger[-i]) + up
    up = plus // 10
    result.append(plus % 10)
    
if up != 0:
    result.append(1)
    
result.reverse()
output = ''
for n in result:
    output = output + str(n)
    
print(output)