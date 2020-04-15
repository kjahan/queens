from src import helper

def solve(chess_board, col_inx):
    for row_inx in range(len(chess_board)):
        chess_board[row_inx][col_inx] = 1
        if helper.is_board_valid(chess_board):
            if col_inx == len(chess_board) - 1:
                # we have a solution
                print("solution: {}".format(chess_board))
            else:
                # move to the next column
                solve(chess_board, col_inx+1)
        chess_board[row_inx][col_inx] = 0


def main():
    chess_board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    solve(chess_board, 0)

main()