# 백준 9184번 문제
# 신나는 함수 실행(동적 계획법)

abc = []

while True:
    input_abc = tuple(map(int, input().split()))
    if input_abc == (-1,-1,-1):
        break
    abc.append(input_abc)

wRecord = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a<b and b<c:
        b1 = b - 1
        c1 = c - 1
        return wRecord[a][b][c1]+wRecord[a][b1][c1]-wRecord[a][b1][c]
    else:
        a1 = a - 1
        b1 = b - 1
        c1 = c - 1
        return wRecord[a1][b][c]+wRecord[a1][b1][c]+wRecord[a1][b][c1]-wRecord[a1][b1][c1]

for a in range(0, 21):
    for b in range(0, 21):
        for c in range(0, 21):
            wRecord[a][b][c] = w(a, b, c)
            
for d in abc:
    print(f'w({d[0]}, {d[1]}, {d[2]}) = {w(d[0],d[1],d[2])}')