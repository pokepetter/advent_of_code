from copy import copy

with open('5_input.txt', 'r') as f:
    text = f.read()

crates, commands = text.split('\n\n')
crates = crates.split('\n')[:-1]
crates = [[l[i] for i in range(1, 35, 4)] for l in crates]
crates = list(zip(*crates)) # turn into columns
crates = [''.join(l).strip() for l in crates]

# [print(e) for e in crates]

commands = commands.strip().split('\n')
# turn 'move 5 from 4 to 5' into [5,4,5]
commands = [[int(word) for word in line.split() if not word in ['move', 'from', 'to']] for line in commands]

def move_crates(crates, has_CrateMover_9001=False):
    for move_amount, from_index, to_index in commands:
        from_index -= 1
        to_index -= 1

        chunk_to_move = crates[from_index][:move_amount]
        crates[from_index] = crates[from_index][move_amount:]   # remove from original stack

        if not has_CrateMover_9001:
            chunk_to_move = chunk_to_move[::-1] # reverse

        crates[to_index] = chunk_to_move + crates[to_index]

    return ''.join([e[0] for e in crates])

print(move_crates(copy(crates)))
print(move_crates(copy(crates), True))
