def has_8queen(board, n):
    temp = 0
    for i in board:
        temp += i.count(1)
    print(temp)
    if temp == n:
        return True
    else:
        return False

def put_queen(board_len):
    chess_board = [[0] * board_len for _ in range(board_len)]

    while True:
        for y in range(board_len):
            for x in range(board_len):
                if chess_board[y][x] == 0:
                    chess_board[y][x] = 1

                    # 가로, 세로, 대각선 방향으로 놓을 수 없는 자리 표시
                    for i in range(board_len):
                        # 가로 놓을 수 없는 자리
                        if chess_board[y][i] == 0:
                            chess_board[y][i] = 2
                        # 세로 놓을 수 없는 자리
                        if chess_board[i][x] == 0:
                            chess_board[i][x] = 2

                        # 오른쪽 아래 처리
                        if y + i < board_len and x + i < board_len and chess_board[y + i][x + i] == 0:
                            chess_board[y + i][x + i] = 2

                        # 왼쪽 위 처리
                        if x - i <= 0 and y - i <= 0 and chess_board[y - i][x - i] == 0:
                            chess_board[y - i][x - i] = 2

                        # 오른쪽 위 처리
                        if y - i >= 0 and x + i < board_len and chess_board[y - i][x + i] == 0:
                            chess_board[y - i][x + i] = 2
                        # 왼쪽 아래 처리
                        if x - i >= 0 and y + i < board_len and chess_board[y + i][x - i] == 0:
                            chess_board[y + i][x - i] = 2

                    for _ in chess_board :
                        print(_)
                    print()
                    if has_8queen(chess_board, 8):
                        return chess_board

    return None

# test
print(put_queen(8))