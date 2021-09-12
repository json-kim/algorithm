# 백준 2004번 문제
# 조합 0의 개수

# n!에서 10이 곱해진 수를 찾으려면 (2*5)몇번 곱해져있는지를 찾아야 한다.
# 1*2*3*...*10에서 5가 곱해진 횟수는 10//5 = 2 이다.
# 단 n이 5의 제곱수(25, 125...)부터는 n//25, n//125... 도 구해주어야 한다. 5가 2개, 3개 들어가는 수이기 때문에
# 5의 배수의 개수, 25의 배수의 개수, 125의 배수의 개수,.... 더해주기
# 2도 똑같이 구해준다.
# 그렇게 찾은 값이 예를들어 5는 5개, 2는 10개라면 10이 곱해진 횟수는 5가 된다.

n, m = map(int, input().split())

def getFactors(n, f):
    factor = f
    count = 0
    while n >= factor:
        count = count + n//factor
        factor = factor * f
    return count

fives = getFactors(n, 5) - getFactors(m, 5) - getFactors(n-m, 5)
twos = getFactors(n, 2) - getFactors(m, 2) - getFactors(n-m, 2)
print(min(fives, twos))
