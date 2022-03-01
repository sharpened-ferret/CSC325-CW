# Neil Woodhouse - 851182

K_VAL = 2
L_VAL = 8
QUEEN_X = (K_VAL % 8) + 1
QUEEN_Y = (L_VAL % 8) + 1

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

    # Marks the position of the fixed piece with a black queen.
    # Other queens will be white pieces to distinguish.
    board[QUEEN_Y - 1][QUEEN_X - 1] = '♛'
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