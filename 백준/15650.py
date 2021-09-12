# 백준 15650번 문제
# N과 M (2)

n, m = map(int, input().split())

#print('n: ',n, ', m: ', m )

# n개중에 m개를 선택하는 재귀함수
def funcA(n, m, last, selectList):
    if len(selectList) == m:
        printList(selectList)
    for i in range(last + 1,n+1):
        if i in selectList:
            continue
        tempList = selectList[:]
        tempList.append(i)
        funcA(n,m, i, tempList)

# 결과 리스트 출력 함수
def printList(list):
    for n in list:
        print(n, end=' ')
    print()

funcA(n, m, 0, [])

# 15649번에서 숫자 중복을 제거해야 함
# 이전에 선택했던 숫자(시작점)을 재귀함수에 전달한다