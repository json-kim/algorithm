# 백준 11051번 문제
# 이항 계수 2

# 이항계수 문제
# n!/(k! * (n-k)!)

N, K = map(int, input().split())

factorial = [0] * (N+1)
factorial[0] = 1
factorial[1] = 1

for i in range(2, N+1):
    factorial[i] = i * factorial[i-1]
    
print(factorial[N]//(factorial[K]*factorial[N-K])%10007)
