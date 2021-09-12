# 백준 15649번 문제
# N과 M (1)

n, m = map(int, input().split())

#print('n: ',n, ', m: ', m )

# n개중에 m개를 선택하는 재귀함수
def funcA(n, m, selectList):
    if len(selectList) == m:
        printList(selectList)
    for i in range(1,n+1):
        if i in selectList:
            continue
        tempList = selectList[:]
        tempList.append(i)
        funcA(n,m,tempList)

# 결과 리스트 출력 함수
def printList(list):
    for n in list:
        print(n, end=' ')
    print()

funcA(n, m, [])

# n, m 
# n, n-1, ..., n-m+1 까지 m개 선택
# 재귀호출해서 n,m,[] 입력하면 1~n중에 하나 선택하는 for문 돌아가고
# 다시 재귀호출해서 n,m,[some]입력하면 1~n중에 some을 제와하고 하나 선택하는 for문 돌아가고
# 다시 재귀호출.. []의 길이가 m과 같으면 프린트
