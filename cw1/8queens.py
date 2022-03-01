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

class Solution:
    queen_positions = []

    def Solution(self):
        self.queen_positions
    
    def is_solved(self):
        if len(self.queen_positions) == 8:
            return True
        return False
    
    # Equality method: returns true if both Solution objects have the same number of queen positions stored, 
    # and have the same queen positions stored (regardless of list order)
    def __eq__(self, other):
        num_equal = 0
        if (len(self.queen_positions) == len(other.queen_positions)):
            for pos in other.queen_positions:
                if self.queen_positions in self.queen_positions:
                    num_equal += 1
            if num_equal == len(self.queen_positions):
                return True
        return False



if __name__ == "__main__":
    main()