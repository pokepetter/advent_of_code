with open('2_input.txt', 'r') as f:
    text = f.read().replace('A','R').replace('B','P').replace('C','S').replace('X','R').replace('Y','P').replace('Z','S')

decrypted_list = [line.split() for line in text.split('\n') if line]

points_from_shape = sum(['RPS'.index(e[1])+1 for e in decrypted_list])

points_from_wins = 0
for their_move, my_move in decrypted_list:
    if their_move == my_move:   # draw
        points_from_wins += 3
    elif (their_move == 'R' and my_move == 'P') or (their_move == 'P' and my_move == 'S') or (their_move == 'S' and my_move == 'R'): # win
        points_from_wins += 6

total_points = points_from_shape + points_from_wins
print('part 1:', total_points)


# part 2
# X = lose, Y = draw, Z = win
points = 0

# correct the decryption
decrypted_list = [[line[0], line[1].replace('R','lose').replace('P','draw').replace('S','win')] for line in decrypted_list]

for their_move, round_result in decrypted_list:
    if round_result == 'draw':
        points += 3
        my_move = their_move

    elif round_result == 'lose':
        my_move = 'SRP'['RPS'.index(their_move)]

    elif round_result == 'win':
        my_move = 'PSR'['RPS'.index(their_move)]
        points += 6

    points += 'RPS'.index(my_move)+1

print('part 2:', points)
