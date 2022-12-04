input_file_name = 'puzzle4_input.txt'

def form_tuples(pair):
    numbers_split = pair.split('-')
    return (int(numbers_split[0]), int(numbers_split[1]))

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        total_pairs = 0
        for l in lines:
            l = l.strip()
            two_pairs = l.split(',')
            first_pair = two_pairs[0]
            second_pair = two_pairs[1]

            first_tuple = form_tuples(first_pair)
            second_tuple = form_tuples(second_pair)

            if (first_tuple[0] == second_tuple[0]) and (first_tuple[1] == second_tuple[1]):
                total_pairs += 1
            elif (first_tuple[0] <= second_tuple[0]) and (first_tuple[1] >= second_tuple[1]):
                total_pairs += 1
            elif (first_tuple[0] >= second_tuple[0]) and (first_tuple[1] <= second_tuple[1]):
                total_pairs += 1
        print(total_pairs)

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        total_pairs = 0
        for l in lines:
            l = l.strip()
            two_pairs = l.split(',')
            first_pair = two_pairs[0]
            second_pair = two_pairs[1]

            first_tuple = form_tuples(first_pair)
            second_tuple = form_tuples(second_pair)

            if (first_tuple[0] == second_tuple[0]) and (first_tuple[1] == second_tuple[1]):
                total_pairs += 1
            elif (first_tuple[0] <= second_tuple[0]) and (first_tuple[1] >= second_tuple[1]):
                total_pairs += 1
            elif (first_tuple[0] >= second_tuple[0]) and (first_tuple[1] <= second_tuple[1]):
                total_pairs += 1
            elif (first_tuple[0] <= second_tuple[0]) and (first_tuple[1] >= second_tuple[0] and first_tuple[1] <= second_tuple[1]):
                total_pairs += 1
            elif (first_tuple[0] >= second_tuple[0] and first_tuple[0] <= second_tuple[1]) and (first_tuple[1] >= second_tuple[1]):
                total_pairs += 1
        print(total_pairs)
part2()