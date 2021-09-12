# 백준 3036번 문제
# 링

# 원의 반지름이 주어지면 
# 첫번째 원과 각 원들의 반지름을 최대공약수로 나눠줘야 한다.
# 유클리드 호제법
# a = bq + r
# a, b의 최대공약수는 b, r의 최대공약수와 같다.
# a = 12, b = 8
# 12 = 8 * 1 + 4
# 8 = 4 * 2 + 0
# r이 0이 되면 종료, b가 최대공약수가 된다.

def getGCD(a, b):
    big = max(a,b)
    sma = min(a,b)
    
    while True:
        r = big%sma
        
        if r == 0:
            break
        big = sma
        sma = r
    
    return sma

n = int(input())
circle = list(map(int, input().split()))

for i in range(1, n):
    cycle = getGCD(circle[0], circle[i])
    print(f'{circle[0]//cycle}/{circle[i]//cycle}')

    
    