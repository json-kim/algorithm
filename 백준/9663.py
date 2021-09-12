# 백준 9663번 문제
# N-Queen
# 파이썬으로는 백트래킹 문제를 시간초과로 인해 수행하기 어려움
n = int(input())
board = [0] * (n*n)
count = [0]

#print('n: ', n)

def funcA(board, queens, count):
    # 모든 줄(행, 또는 열)에 퀸이 하나씩 채워졌을 때 
    if len(queens) == n:
        count[0] = count[0] + 1
        return
    
    # len(queens)는 몇번째 행인지를, queens의 원소들은 선택된 열의 번호 리스트를 나타낸다.
    # 따라서 다음 행의 선택되지 않은 열에 해당하는 칸에서만 배치가 가능한지를 체크하고 가능할 경우에만
    # 다시 재귀를 호출하여 다음 칸을 찾아간다. 
    for i in [x for x in list(range(0,n)) if x not in queens]:
        print('행: ', len(queens)+1,'열: ',i+1)
        if check(len(queens), i, board, n):
            print('가능')
            tempBoard = board[:]
            tempBoard[len(queens)*n+i] = 1
            tempQueens = queens[:]
            tempQueens.append(i)
            funcA(tempBoard, tempQueens, count)
        else:
            continue
    
# (x, y)칸에 있는 말을 보드판에 안겹치게 배치할 수 있는지 판단하는 함수
def check(x, y, board, n):
    # 같은 가로줄 체크
    # if 1 in board[x*n:(x+1)*n]:
    #     return False
    # 같은 세로줄 체크
    # if 1 in board[(n*x+y) for x in list(range(n))]:
    #     return False
        
    # 대각선(좌상) 체크
    for i in range(1, n):
        nx = x - i
        ny = y - i
        if nx < 0 or ny <0:
            break
        if board[nx*n+ny] == 1:
            return False
    # 대각선(우하) 체크
    # for i in range(1, n):
    #     nx = x + i
    #     ny = y + i
    #     if nx > n - 1 or ny > n - 1:
    #         break
    #     if board[nx*n+ny] == 1:
    #         return False
    # 대각선(우상) 체크
    for i in range(1, n):
        nx = x - i
        ny = y + i
        if nx < 0 or ny > n - 1:
            break
        if board[nx*n+ny] == 1:
            return False
    # 대각선(좌하) 체크
    # for i in range(1, n):
    #     nx = x + i
    #     ny = y - i
    #     if nx > n - 1 or ny < 0:
    #         break
    #     if board[nx*n+ny] == 1:
    #         return False
    # 위의 경우에 해당하지 않을 때 True 리턴
    return True

funcA(board, [], count)
print(count[0])
# n x n 체스판에서 n개의 퀸을 서로가 공격할 수 없도록 배치하는 경우의 수
# 퀸은 가로,세로,대각선 모두 공격 가능 => 가로,세로,대각에서 마주치게 않게 배치
# (0,0)(0,1)(0,2)
# (1,0)(1,1)(1,2)
# (2,0)(2,1)(2,2)
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# 각 행,렬에는 퀸이 하나씩은 꼭 들어가야 n개의 퀸을 배치할 수 있다. 
# 그렇다면 모든 칸을 대상으로 재귀함수를 호출할게 아니라 다음 줄의 n개의 칸 중에서 선택하기로 하면 호출하는 횟수가 n*n이 된다.
# 이 방법으로 진행할 시 같은 가로줄 체크, 세로줄 체크, 우하, 좌하 체크는 안해도 된다.
# 좌상, 우상만 퀸이 있는지 체크한다.