board_size = 5

board = [[0 for x in range(board_size)] for y in range(board_size)]
print("0 A B C D E")
for row in range(board_size):
    print(row+1, " ".join(str(board[row][col]) for col in range(board_size)))