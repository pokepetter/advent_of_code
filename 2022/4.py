with open('4_input.txt', 'r') as f:
    all_pairs = [l for l in f.read().split('\n') if l]

pairs_with_complete_overlap = 0
pairs_with_some_overlap = 0

for pair in all_pairs:
    pair = pair.split(',')

    for i, assignment in enumerate(pair):
        assignment = assignment.split('-')
        assignment = [int(e) for e in assignment]
        assignment = tuple(range(assignment[0], assignment[1]+1))   # convert start and end to a tuple of all the numbers
        pair[i] = assignment

    first, second = pair
    # check if second contains all of first or first contains all of second and increment if it does
    pairs_with_complete_overlap += int(all(e in first for e in second) or all(e in second for e in first))
    # same, but with any overlap
    pairs_with_some_overlap += int(any(e in first for e in second))

print(pairs_with_complete_overlap)
print(pairs_with_some_overlap)
