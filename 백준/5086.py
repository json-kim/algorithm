# 백준 5086번 문제
# 배수와 약수

import sys

case = []

while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break
    case.append([a, b])
    
for c in case:
    if c[0] % c[1] == 0:
        print('multiple')
    elif c[1] % c[0] == 0:
        print('factor')
    else:
        print('neither')
