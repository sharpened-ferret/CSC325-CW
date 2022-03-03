# Neil Woodhouse - 851182

import random

 # Calculates the position for the fixed queen
K_VAL = 2
L_VAL = 8
QUEEN_X = (K_VAL % 8) + 1
QUEEN_Y = (L_VAL % 8) + 1

 # Stores the position of the fixed queen as a tuple in the 0-7 coordinate space
FIXED_QUEEN_ARR_POS = (QUEEN_X-1, QUEEN_Y-1)

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
    starting_positions = []
    unassigned_queens = 7
    for x in range(0, 8):
        if (x+1 != QUEEN_X):
            rand_y = random.randint(0, 7)
            board[rand_y][x] = WHITE_QUEEN
            starting_positions.append((x, rand_y))
            unassigned_queens -= 1
    print_board(board)
    print("Starting Positions (0-7 coords):" + str(starting_positions))
    
    test_node = Node(None, starting_positions)
    print(test_node.h)

    solution_path = astar(starting_positions)
    if (solution_path is not None):
        print("Safe Position Found...")
        for node in solution_path:
            print(node)
    else:
        print("No solutions found...")
    


def astar(queen_positions):
    starting_node = Node(None, queen_positions)

    open_list = []
    closed_list = []

    open_list.append(starting_node)

    while(len(open_list) > 0):
        curr_node = open_list[0]
        open_list.remove(curr_node)
        closed_list.append(curr_node)
        print(str(curr_node.queen_positions) + "Num Threatened: " + str(curr_node.h))
        convert_board(curr_node.queen_positions)

         # If the current state has all Queens in safe positions, return it
        if curr_node.h == 0:
            move_path = []
            curr = curr_node 
            while curr is not None:
                move_path.append(curr.queen_positions)
                curr = curr.parent
            return move_path[::-1]

        curr_node.gen_children()
        for child in curr_node.children:
            new_state = True
            for closed_node in closed_list:
                if child == closed_node:
                    new_state = False
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    new_state = False
            if child.h > curr_node.h: # TODO remove this test later
                new_state = False 
            if new_state:
                open_list.append(child)
        open_list.sort(key=safe_queen_sort, reverse=False)
        open_list_h = []
        for item in open_list:
            open_list_h.append(item.h)
        print(open_list_h)
    
def convert_board(path):
    output_board = [
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢']
    ]
    output_board[FIXED_QUEEN_ARR_POS[1]][FIXED_QUEEN_ARR_POS[0]] = BLACK_QUEEN
    for pos in path:
        output_board[pos[1]][pos[0]] = WHITE_QUEEN
    print_board(output_board)


def print_board(board):
    output_board = board.copy()
    output_board.reverse()
    for row in output_board:
        print(''.join(row))

def safe_queen_sort(node):
    return node.h

def print_tuple(tuple_pos):
    return "({}, {})".format(tuple_pos[0] + 1, tuple_pos[1] + 1)

class Node:
    def __init__(self, parent, queen_positions):
        self.parent = parent
        self.children = []
        self.queen_positions = queen_positions

        if parent is None:
            self.g = 0
        else:
            self.g = self.parent.g + 1
        self.h = self.threatened_queen_num()
        self.f = self.g + self.h

    def __str__(self):
        return "parent=[{}], fixed queen={}, queens={}, safe={}".format(self.parent, (QUEEN_X, QUEEN_Y), self.queen_positions, 8-self.h)

    def __repr__(self):
        return self.__str__()+"\n"

    def __eq__(self, other):
        if len(self.children) == len(other.children):
            num_matching = 0
            for node in other.children:
                if node in self.children:
                    num_matching += 1
            if num_matching == len(self.children):
                return True
        return False

     # The number of queens in safe positions is used as a success heuristic
    def threatened_queen_num(self):
        # TODO calculate number of safe queens
        safe_queen_num = 8
        combined_queens = self.queen_positions.copy()
        combined_queens.append(FIXED_QUEEN_ARR_POS)
        for queen in combined_queens:
            is_safe = True
            other_queens = combined_queens.copy()
            other_queens.remove(queen)
            for other in other_queens:
                 # Checks if another queen exists in the same row or col
                if queen[0] == other[0] or queen[1] == other[1]:
                    is_safe = False
                    break
            for i in range(-7, 7):
                 # Checks diagonal directions through the board
                coord = (queen[0]+i, queen[1]+i)
                if coord in other_queens:
                    is_safe = False
                    break
                coord = (queen[0]+i, queen[1]-i)
                if coord in other_queens:
                    is_safe = False
                    break
            if not is_safe:
                # print("Queen at {} threatened".format(print_tuple(queen)))
                safe_queen_num -= 1
        return (8 - safe_queen_num)

    def get_moves(self, curr_pos):
        valid_moves = []
        blocked_positions = self.queen_positions.copy()
        blocked_positions.remove(curr_pos)
        blocked_positions.append(FIXED_QUEEN_ARR_POS)
        for n in range(0, 8):
            if n != curr_pos[0]:
                valid_moves.append((n, curr_pos[1]))
            if n != curr_pos[1]:
                valid_moves.append((curr_pos[0], n))
        for n in range(-7, 7):
             # Calculates y=x diagonal moves
            diagonal_pos = (curr_pos[0]+n, curr_pos[1]+n)
            if (diagonal_pos[0] in range(0,8) and diagonal_pos[1] in range(0,8)):
                valid_moves.append(diagonal_pos)

             # Calculates y=-x diagonal moves
            diagonal_pos = (curr_pos[0]+n, curr_pos[1]-n)
            if (diagonal_pos[0] in range(0,8) and diagonal_pos[1] in range(0,8)):
                valid_moves.append(diagonal_pos)
        for pos in blocked_positions:
            if pos in valid_moves:
                valid_moves.remove(pos)
        return valid_moves

    
     # Checks if a solution has been found (if all queens are safe)
    def is_solved(self):
        if self.h == 0:
            return True
        return False

    def gen_children(self):
        children = []
         # TODO Check for all safe positions that children can be placed in
        for i in range(len(self.queen_positions)):
            curr_queen = self.queen_positions[i]
            other_queens = self.queen_positions.copy()
            other_queens.pop(i)
            # TODO Generate children at possible positions
            curr_moves = self.get_moves(curr_queen)
            for move in curr_moves:
                new_queen_positions = other_queens.copy()
                new_queen_positions.append(move)
                children.append(
                    Node(self, new_queen_positions)
                )
        self.children = children



if __name__ == "__main__":
    main()