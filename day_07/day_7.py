input_file_name = 'puzzle7_input.txt'

commands = ['$ cd', '$ ls', "dir "]

def generate_tree_from_input(lines):
    root = None
    current_node = None

    for l in lines:
        l = l.strip()
        if root == None and commands[0] in l:
            root = (l.split(commands[0])[1], 'root', [], None, 0)
            current_node = root
            print('Root node', root)
            continue

        if commands[1] in l:
            continue
        elif commands[0] in l:
            name = l.split(commands[0])[1].strip()
            if name == '..':
                current_node = current_node[1]
            else:
                for child in current_node[2]:
                    if name == child[0]:
                        current_node = child
                        break
        else:
            if commands[2] in l:
                new_node_name = l.split(commands[2])[1]
                current_node[2].append((new_node_name, current_node, [], None, 0))
            else:
                content = l.split()
                current_node[2].append((None, current_node, [], content, 0))
    return root

def solve(node, below, threshold):
    if node is not None:
        if node[3] != None:
            return (int(node[3][0]), below, threshold)

        numbers = []
        for child in node[2]:
            temp = solve(child, below, threshold)
            numbers.append(temp[0])
        
        s_temp = sum(numbers)

        if (s_temp > threshold):
            below.append(s_temp)
        return (s_temp, below, threshold)

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        root_node = generate_tree_from_input(lines)
        total = solve(root_node, [], 100000)
        print('Total', total[0])
        print('All Under 100000', total[1])
        print('Sum', sum(total[1]))

def part2():
    total_disk_space = 70000000
    needed_space = 30000000
    with open(input_file_name) as f:
        lines = f.readlines()
        root_node = generate_tree_from_input(lines)
        threshold = 100000
        total = solve(root_node, [], threshold)
        space_left = total_disk_space - total[0]
        print('Space Left', space_left)

        min_total_to_delete = needed_space - space_left
        print('Min Total to Delete', min_total_to_delete)

        total = solve(root_node, [], min_total_to_delete)
        print('Total', total[0])
        print(f'All Under {min_total_to_delete}', total[1])
        print('Min of "All Under"', min(total[1]))

part2()