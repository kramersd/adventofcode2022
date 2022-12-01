input_file_name = 'puzzle1_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        elf = []
        elves = []
        for l in lines:
            if not l.strip():
                elves.append(sum(elf))
                elf = []
            else:
                elf.append(int(l.strip()))
        print(max(elves))

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        elf = []
        elves = []
        for l in lines:
            if not l.strip():
                elves.append(sum(elf))
                elf = []
            else:
                elf.append(int(l.strip()))
        print(sum(sorted(elves)[-3:]))
part2()