# 백준 9251번 문제
# LCS (동적 계획법)

# 최장 공통 부분 수열
# 이 문제는 두 문자열의 길이를 한칸씩 늘려가며 최장공통부분수열의 길이를 표로 그려가며
# 규칙을 찾아야 한다.

A = input()
B = input()

lcs = [[0]*(len(A)+1) for _ in range(len(B)+1)]

for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if A[j-1] == B[i-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            
print(lcs[-1][-1])