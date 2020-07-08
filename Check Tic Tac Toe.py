"""
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe board.
However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves
were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space,
and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any.
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
"""

PLAYER_1 = 1
PLAYER_2 = 2

def checkTicTacToe(matrix, size):
    size = len(matrix)
    result = ""
    p1_diag1 = 0
    p2_diag1 = 0
    p1_diag2 = 0
    p2_diag2 = 0

    for i in range(0,size):
        p1_rows = 0
        p2_rows = 0
        p1_columns = 0
        p2_columns = 0

        for j in range(0,size):
            # Check Row
            if matrix[i][j] == PLAYER_1:
                p1_rows += matrix[i][j]
            else:
                p2_rows += matrix[i][j]

            # Check Column
            if matrix[j][i] == PLAYER_1:
                p1_columns += matrix[j][i]
            else:
                p2_columns += matrix[j][i]

        if p1_rows == PLAYER_1* size or p1_columns == PLAYER_1*size:
            return "P1 is winner"
        elif p2_rows == PLAYER_2* size or p2_columns == PLAYER_2*size:
            return "P2 is winner"
        # Check Diagonal 1
        if matrix[i][i] == PLAYER_1:
            p1_diag1 += matrix[i][i]
        else:
            p2_diag1 += matrix[i][i]
        # Check Diagonal 2

        if matrix[i][size-1-i] == PLAYER_1:
            p1_diag2 += matrix[i][size-1-i]
        else:
            p2_diag2 += matrix[i][size-1-i]
    print(p1_diag1," ",p2_diag1," ",p1_diag2," ",p2_diag2)
    if p1_diag1 == PLAYER_1* size or p1_diag2 == PLAYER_1*size:
        return "P1 is winner"
    elif p2_diag1 == PLAYER_2* size or p2_diag2 == PLAYER_2*size:
        return "P2 is winner"
    else:
        return "There's no winner"





matrix_1=[[2,2,2,1,1],
          [1,2,1,1,2],
          [2,2,2,1,1],
          [1,2,2,2,2],
          [1,1,2,2,2]]

matrix_2 = [[2,2],
            [2,1]]
matrix_3 =[[1]]
print(checkTicTacToe(matrix_1,4))
print(checkTicTacToe(matrix_2,2))
print(checkTicTacToe(matrix_3,2))