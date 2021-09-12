# 백준 2580번 문제
# 스도쿠

# 9x9 칸의 스도쿠 보드
# 가로,세로줄에는 1~9까지의 숫자가 한번씩만 들어가야함
# 굵은 줄로 쳐진 3x3칸의 사각형에는 1~9까지의 숫자가 한번씩만 들어가야함
result = []
# 보드결과값 출력 함수
def printBoard(board):
    for row in board:
        for num in row:
            print(num, end=' ')
        print()

# board의 (row, col)칸에 num 숫자가 적합한지를 체크하는 함수
def check(row, col, board, num):
    # 가로줄 체크
    if num in board[row]:
        return False
    # 세로줄 체크
    for i in range(9):
        if num == board[i][col]:
            return False
    # 사각형 체크
    sqRow = row//3
    sqCol = col//3
    for r in range(3):
        for c in range(3):
            if num == board[sqRow*3+r][sqCol*3+c]:
                return False
    return True

# 백트래킹을 수행할 재귀함수
def sudoku(emptyCells, idx, board, result):
    # 빈칸을 다 채웠을 경우 더 이상 재귀호출하지 않고 종료
    if len(emptyCells) == idx:
        result.append(board)
        return
    # 빈칸이 남았을 경우
    for num in range(1,10):
        cell = emptyCells[idx]
        if check(cell[0], cell[1], board, num):
            tempBoard = board[:]
            tempBoard[cell[0]][cell[1]] = num
            sudoku(emptyCells, idx+1, tempBoard, result)
        else:
            continue

# 보드판에서 빈칸을 찾아 리스트로 리턴
def findEmptyCell(board):
    emptyCells = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                emptyCells.append((row, col))
    return emptyCells


    

board = []
# 스도쿠 보드판 입력받기
for _ in range(9):
    board.append(list(map(int, input().split())))
 
# 스도쿠보드의 빈칸 리스트
emptyCells = findEmptyCell(board)

# 빈칸 채우기 알고리즘
sudoku(emptyCells, 0, board, result)
if len(result) != 0:
    printBoard(result)
