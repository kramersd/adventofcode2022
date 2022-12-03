input_file_name = 'puzzle3_input.txt'

import string

alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

alpha_lower_numbers = {}
alpha_upper_numbers = {}

def setup_alphabet():
    number = 1
    for i in alphabet_lower:
        alpha_lower_numbers[i] = number
        number += 1
    
    number = 27
    for i in alphabet_upper:
        alpha_upper_numbers[i] = number
        number += 1

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        shared_items = []
        for l in lines:
            l = l.strip()
            half = int(len(l) / 2)
            first = l[:half]
            second = l[half:]

            unique_items = []
            for i in first:
                if i in second:
                    if i not in unique_items:
                        unique_items += i
            shared_items.extend(unique_items)
        total = 0
        for item in shared_items:
            if item in alpha_lower_numbers:
                total += alpha_lower_numbers[item]
            elif item in alpha_upper_numbers:
                total += alpha_upper_numbers[item]
            else:
                print('Unknown item', item)
        print(shared_items)
        print(total)
    
def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        groups_of_three = []
        single_group = []
        iteration = 0
        for i in range(len(lines)):
            line = lines[i].strip()
            if iteration == 2:
                single_group.append(line)
                groups_of_three.append(single_group)
                single_group = []
                iteration = 0
            else:
                single_group.append(line)
                iteration += 1

        badges = {}
        for j in range(len(groups_of_three)):
            all_letters = {}
            uniques = []
            for rucksack in groups_of_three[j]:
                unique_letters = {}
                for letter in rucksack:
                    if letter not in unique_letters:
                        unique_letters[letter] = 1
                uniques.append(unique_letters)

            all_letters = {}
            for u in uniques:
                for i in u.keys():
                    all_letters[i] = all_letters.get(i, 0) + 1
            
            for (k,v) in all_letters.items():
                if v == 3:
                    badges[j] = k
        
        total = 0
        for (k,v) in badges.items():
            if v in alpha_lower_numbers:
                total += alpha_lower_numbers[v]
            elif v in alpha_upper_numbers:
                total += alpha_upper_numbers[v]
            else:
                print('Unknown item', v)
        print(total)

setup_alphabet()
part2()