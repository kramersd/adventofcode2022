input_file_name = 'puzzle5_input.txt'

columns_indexes = [1,5,9,13,17,21,25,29,33]
board_key_line_num = 9

def reverse_order(temp):
    x = []
    for i in range(len(temp)):
        x.append(temp.pop())
    return x

def print_board(board_stacks):
    i = 1
    for bs in board_stacks:
        print(i, 'BS', bs)
        i += 1

def read_input(lines):
    board = []
    moves = []
    for l in lines:
        x = []
        if 'move' not in l:
            for letter in l:
                if letter != '\n':
                    x.append(letter)
            board.append(x)
        if 'move' in l:
            l = l.strip().replace('move', '').replace('from', '').replace('to', '').split()
            moves.append(l)
    return (board,moves)

def setup_board_stacks(board):
    board_stacks = []
    for i in range(0,board_key_line_num):
        board_stacks.append([])
    
    for i in range(len(columns_indexes)):
        for j in range(board_key_line_num - 2,-1,-1):
            if board[j][columns_indexes[i]] != ' ':
                board_stacks[i].append(board[j][columns_indexes[i]])
    return board_stacks

def get_top_crates(board_stacks):
    top_crates = ''
    for bs in board_stacks:
        top_crates += (bs[len(bs) -1])
    return top_crates

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        (board, moves) = read_input(lines)
        board_stacks = setup_board_stacks(board)
        for move in moves:
            for i in range(int(move[0])):
                board_stacks[int(move[2]) - 1].append(board_stacks[int(move[1]) -1].pop())
        print_board(board_stacks)
        print(get_top_crates(board_stacks))

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        (board, moves) = read_input(lines)
        board_stacks = setup_board_stacks(board)
        print('Number of moves', len(moves))
        for move in moves:
            temp = []
            for i in range(int(move[0])):
                temp.append(board_stacks[int(move[1]) -1].pop())
            temp = reverse_order(temp)
            board_stacks[int(move[2]) - 1].extend(temp)
        print_board(board_stacks)
        print(get_top_crates(board_stacks))

part2()