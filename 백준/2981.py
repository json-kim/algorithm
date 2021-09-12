# 백준 2981번 문제
# 검문

import math

# a = m*A + r
# b = m*B + r
# a-b = m(A-B)
# m은 위의 식들을 만족해야 한다.
# A-B가 정수이기 때문에 m은 a-b의 약수가 된다.
# ex)6, 34: 34 - 6 = 28, m은 28의 약수이다. 2, 4, 7, 28
# m은 a-b의 약수로 볼 수 있다.
# 입력 값이 3개일 때
# 첫번째 두번째 뺄셈값의 약수이면서 두번째 세번째 뺄셈값의 약수인 공약수가 가능한 m의 개수가 된다.(M>1)

def getGcd(a,b):
    big = max(a,b)
    sma = min(a,b)
    r = 0
    while big%sma != 0:
        r = big % sma
        big = sma
        sma = r
        
    return sma

n = int(input())
case = []

for _ in range(n):
    case.append(int(input()))

case2 = []

for i in range(n-1):
    case2.append(abs(case[i+1]-case[i]))

gcd = case2[0]

for i in range(1,len(case2)):
    gcd = getGcd(gcd, case2[i])
    
result = [gcd]
for i in range(2, int(math.sqrt(gcd))+1):
    if gcd%i == 0:
        result.append(i)
        result.append(gcd//i)
        
result = list(set(result))
result.sort()

for i in result:
    print(i, end=' ')
    