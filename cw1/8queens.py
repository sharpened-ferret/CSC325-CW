# Neil Woodhouse - 851182

import random

K_VAL = 2
L_VAL = 8
QUEEN_X = (K_VAL % 8) + 1
QUEEN_Y = (L_VAL % 8) + 1

 # Sets the characters for marking white and black queens
BLACK_QUEEN = '♛'
WHITE_QUEEN = '♕'

def main():
    print("Problem Started, Fixed Queen Position = ({}, {})\n".format(QUEEN_X, QUEEN_Y))
    print("(Fixed queen Marked in Black)")

    board = [
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢']
    ]

    # Marks the position of the fixed piece with a black queen
    board[QUEEN_Y - 1][QUEEN_X - 1] = BLACK_QUEEN

    # Randomly assigns the other 7 queens, marked with white queens
    unassigned_queens = 7
    while unassigned_queens > 0:
        rand_x = random.randint(0, 7)
        rand_y = random.randint(0, 7)

        curr_pos = board[rand_y][rand_x]
        if curr_pos != BLACK_QUEEN or curr_pos != WHITE_QUEEN:
            board[rand_y][rand_x] = WHITE_QUEEN
            unassigned_queens -= 1
    print_board(board)
    

def print_board(board):
    for row in board:
        print(''.join(row))

class Node:
    def Node(self, parent, board):
        self.parent = parent
        self.children = []
        self.board = board

        self.g = self.parent.g + 1
        self.h = self.safe_queens()
        self.f = self.g + self.h

     # The number of queens in safe positions is used as a success heuristic
    def safe_queens():
        # TODO calculate number of safe queens
        return 0
    
     # Checks if a solution has been found (if all queens are safe)
    def is_solved(self):
        if self.h == 8:
            return True
        return False

    def gen_children(self):
         # TODO Check for all safe positions that children can be placed in
        return



if __name__ == "__main__":
    main()