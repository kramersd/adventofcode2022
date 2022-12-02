input_file_name = 'puzzle2_input.txt'

p1_outcomes = {
    ('A', 'X'): 3, # draw
    ('A', 'Y'): 6, # User wins
    ('A', 'Z'): 0, # User loses
    
    ('B', 'Y'): 3, # draw
    ('B', 'X'): 0, # User loses
    ('B', 'Z'): 6, # User wins

    ('C', 'Z'): 3, # draw
    ('C', 'X'): 6, # User wins
    ('C', 'Y'): 0, # User loses
}

p1_shape_key = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

p2_answer_key = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

p2_outcomes = {
    # (Opponent, How Round Ends): (round_score, what you must play, letter of choice, shape_score)

    # Rock
    ('A', 'X'): (0, 'Scissors', 'Z', 3), # User loses
    ('A', 'Y'): (3, 'Rock',     'X', 1), # User draws
    ('A', 'Z'): (6, 'Paper',    'Y', 2), # User wins
    
    # Paper
    ('B', 'X'): (0, 'Rock',     'Z', 1), # User loses
    ('B', 'Y'): (3, 'Paper',    'X', 2), # User draws
    ('B', 'Z'): (6, 'Scissors', 'Y', 3), # User wins

    # Scissors
    ('C', 'X'): (0, 'Paper',    'Z', 2), # User loses
    ('C', 'Y'): (3, 'Scissors', 'X', 3), # User draws
    ('C', 'Z'): (6, 'Rock',     'Y', 1), # User wins
}

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        total_score = 0
        for l in lines:
            letters = l.split(' ')
            opponent = letters[0].strip()
            user = letters[1].strip()

            round_score = p1_shape_key[user] + p1_outcomes[(opponent, user)]
            total_score += round_score
        print(total_score)
    
def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        total_score = 0
        for l in lines:
            letters = l.split(' ')
            opponent = letters[0].strip()
            round_outcome = letters[1].strip()

            round_score_metadata = p2_outcomes[(opponent, round_outcome)]
            round_score = round_score_metadata[0] + round_score_metadata[3]
            total_score += round_score

        print(total_score)
part2()