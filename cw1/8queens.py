# Neil Woodhouse - 851182

import random
import copy

 # Calculates the position for the fixed queen
K_VAL = 2
L_VAL = 8
QUEEN_X = (K_VAL % 8) + 1
QUEEN_Y = (L_VAL % 8) + 1

QUEEN_ARRAY_POS = QUEEN_X - 1

 # Stores the position of the fixed queen as a tuple in the 0-7 coordinate space
FIXED_QUEEN_ARR_POS = (QUEEN_X-1, QUEEN_Y-1)

 # Sets the characters for marking white and black queens
BLACK_QUEEN = '♛'
WHITE_QUEEN = '♕'

 # Stops execution early once all solutions have been found
TIMEOUT_VAL = 16

 # An empty chessboard for use in rendering
EMPTY_BOARD = [
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢'],
        ['▢', '▨', '▢', '▨', '▢', '▨', '▢', '▨'],
        ['▨', '▢', '▨', '▢', '▨', '▢', '▨', '▢']
    ]

class Node:
    def __init__(self, parent, queen_positions, active_queen):
        self.parent = parent
        self.children = []
        self.queen_positions = queen_positions
        self.active_queen = active_queen

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
        # if len(self.children) == len(other.children):
        #     num_matching = 0
        #     for node in other.children:
        #         if node in self.children:
        #             num_matching += 1
        #     if num_matching == len(self.children):
        #         return True
        if self.queen_positions == other.queen_positions:
            return True
        return False

     # The number of queens in safe positions is used as a success heuristic
    def threatened_queen_num(self):
        # TODO calculate number of safe queens
        safe_queen_num = 8
        for queen in self.queen_positions:
            is_safe = True
            other_queens = copy.deepcopy(self.queen_positions)
            other_queens.remove(queen)
            for other in other_queens:
                 # Checks if another queen exists in the same row or col
                if queen[0] == other[0] or queen[1] == other[1]:
                    is_safe = False
                    break
            for i in range(-7, 8):
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
        for n in range(0, 8):
            if n != curr_pos[1]:
                valid_moves.append((curr_pos[0], n))
        # print("Valid Moves: {}".format(valid_moves))
        return valid_moves

    def gen_children(self, active_queen):
        children = []
        movable_queens = [0,1,3,4,5,6,7]
        for i in movable_queens:
            start_pos = self.queen_positions[i]
            available_moves = self.get_moves(start_pos)
            # print(i)

            for move in available_moves:
                # print("Current Move: {} for active queen: {}".format(move, active_queen))
                new_queen_positions = copy.deepcopy(self.queen_positions)
                # print(new_queen_positions)
                new_queen_positions[i] = move
                next_active = random.randint(0, 7)
                if next_active == QUEEN_ARRAY_POS:
                    next_active = (next_active + 1) % 8
                children.append(Node(self, new_queen_positions, next_active))
        self.children = children

 # Takes an array of tuples representing the positions of the non-fixed queens (in a 0-7 coordinate space)
def astar(queen_positions):
    starting_node = Node(None, queen_positions, 0)

    open_list = []
    closed_list = []
    open_list.append(starting_node)

    while len(open_list) > 0:
        curr_node = open_list[0]
        open_list.pop(0)
        closed_list.append(curr_node)

        print("Queen Positions={} Threatened Queens={}".format(curr_node.queen_positions, curr_node.h))

        if curr_node.h == 0:
            move_path = []
            curr = curr_node
            while curr.parent is not None:
                move_path.append(curr.queen_positions)
                curr = curr.parent
            return move_path[::-1]
        
        curr_node.gen_children(curr_node.active_queen)
        for child in curr_node.children:
            new_state = True
            if child in closed_list:
                new_state = False
            if child in open_list:
                new_state = False
            if new_state:
                open_list.append(child)
        open_list.sort(key=threatened_queen_sort, reverse=False)

def astar_multi(queen_positions):
    starting_node = Node(None, queen_positions, 0)
    solution_nodes = []

    open_list = []
    closed_list = []
    open_list.append(starting_node)

    while len(open_list) > 0 and len(solution_nodes) < TIMEOUT_VAL:
        curr_node = open_list[0]
        open_list.pop(0)
        closed_list.append(curr_node)

        print("Queen Positions={}, Threatened Queens={}, Found Solutions={}".format(curr_node.queen_positions, curr_node.h, len(solution_nodes)))

        if curr_node.h == 0:
            solution_nodes.append(curr_node)
        
        curr_node.gen_children(curr_node.active_queen)
        for child in curr_node.children:
            new_state = True
            if child in closed_list:
                new_state = False
            if child in open_list:
                new_state = False
            if new_state:
                open_list.append(child)
        open_list.sort(key=threatened_queen_sort, reverse=False)
    return solution_nodes



def print_tuple(tuple_pos):
    return "({}, {})".format(tuple_pos[0] + 1, tuple_pos[1] + 1)

def threatened_queen_sort(node):
    return node.h

def print_board(queen_positions):
    output_board = copy.deepcopy(EMPTY_BOARD)
    for pos in queen_positions:
        output_board[pos[1]][pos[0]] = WHITE_QUEEN
    output_board[FIXED_QUEEN_ARR_POS[1]][FIXED_QUEEN_ARR_POS[0]] = BLACK_QUEEN
    output_board.reverse()
    for row in output_board:
        print(''.join(row))

def main():
    print("Problem Started, Fixed Queen Position = ({}, {})\n".format(QUEEN_X, QUEEN_Y))

    starting_positions = [
        None,
        None, 
        None,
        None,
        None,
        None,
        None,
        None
    ]
    unassigned_queens = 7
    for x in range(0, 8):
        if (x != QUEEN_ARRAY_POS):
            rand_y = random.randint(0, 7)
            starting_positions[x] = (x, rand_y)
            unassigned_queens -= 1
    starting_positions[QUEEN_ARRAY_POS] = FIXED_QUEEN_ARR_POS
    print("Starting Positions:")
    for pos in starting_positions:
        print("({}, {})".format(pos[0]+1, pos[1]+1))

    move_path = astar(starting_positions)
    if move_path is not None:
        print("Single Solution Complete - Printing required moves:")
        for move in move_path:
            print_board(move)
            print("\n")

    print("Single Solution Complete, starting multiple solutions\n")  
    multi_solutions = astar_multi(starting_positions)
    if multi_solutions is not None:
        print("All Solutions Found - Printing each final position.")
        for solution in multi_solutions:
            print_board(solution.queen_positions)
            print("\n")
    

if __name__ == "__main__":
    main()