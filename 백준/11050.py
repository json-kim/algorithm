# 백준 11050번 문제
# 이항 계수 1

# 이항계수 이항식으로 전개했을 때의 계수를 구하는 방식으로 
# 조합의 정의와 일치한다.
# n!/k!*(n-k)!
N, K = map(int, input().split())

factorial = [0] * (N+1)
factorial[0] = 1
factorial[1] = 1

for i in range(2, N+1):
    factorial[i] = i*factorial[i-1]
    
print(factorial[N]//(factorial[K]*factorial[N-K]))