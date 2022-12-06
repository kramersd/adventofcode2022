input_file_name = 'puzzle6_input.txt'

def part1():
    with open(input_file_name) as f:
        start_of_packet_length = 4
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            print('Len of Line', len(l))
            for i in range(len(l)):
                if i + 14 > len(l) - 1:
                    print(i)
                else:
                    stack = {}
                    for j in range(start_of_packet_length):
                        if l[i + j] not in stack:
                            stack[l[i + j]] =  1
                        else:
                            stack = {}
                            break
                        if len(stack.keys()) == start_of_packet_length:
                            print('First Stack of Packet Marker Position:', i + j + 1)
                            return

def part2():
    with open(input_file_name) as f:
        start_of_packet_length = 14
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            print('Len of Line', len(l))
            for i in range(len(l)):
                if i + 14 > len(l) - 1:
                    print(i)
                else:
                    stack = {}
                    for j in range(start_of_packet_length):
                        if l[i + j] not in stack:
                            stack[l[i + j]] =  1
                        else:
                            stack = {}
                            break
                        if len(stack.keys()) == start_of_packet_length:
                            print('First Stack of Packet Marker Position:', i + j + 1)
                            return
part1()
part2()