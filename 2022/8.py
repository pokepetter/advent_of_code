with open('8_input.txt', 'r') as f:
    trees = f.read().strip().split('\n')
#     trees = '''
# 30373
# 25512
# 65332
# 33549
# 35390'''.strip().split('\n')

trees = [[int(char) for char in line] for line in trees]
h = len(trees)
w = len(trees[0])

visible_trees = [[0 for e in row] for row in trees]

for y in range(h):
    tallest_tree_so_far = trees[y][0]
    visible_trees[y][0] = 1
    for x in range(w):  # search from left
        if trees[y][x] > tallest_tree_so_far:
            visible_trees[y][x] = 1
            tallest_tree_so_far = trees[y][x]

for y in range(h):
    tallest_tree_so_far = trees[y][w-1]
    visible_trees[y][w-1] = 1
    for x in range(w-1, 0, -1):     # search from right
        if trees[y][x] > tallest_tree_so_far:
            visible_trees[y][x] = 1
            tallest_tree_so_far = trees[y][x]

for x in range(w):
    tallest_tree_so_far = trees[0][x]
    visible_trees[0][x] = 1
    for y in range(h):      # search from top
        if trees[y][x] > tallest_tree_so_far:
            visible_trees[y][x] = 1
            tallest_tree_so_far = trees[y][x]

for x in range(w):
    tallest_tree_so_far = trees[h-1][x]
    visible_trees[h-1][x] = 1
    for y in range(h-1, 0, -1):     # search from bottom
        if trees[y][x] > tallest_tree_so_far:
            visible_trees[y][x] = 1
            tallest_tree_so_far = trees[y][x]

# [print(''.join([str(_) for _ in e])) for e in visible_trees]

visible_count = sum([sum(e) for e in visible_trees])
print('part 1:', visible_count)

view_scores = [[0 for e in row] for row in trees]

# part 2
highest_score = 0

for y in range(h):
    for x in range(w):

        right = 0
        for temp_x in range(x+1, w):
            right += 1
            if trees[y][temp_x] >= trees[y][x]:
                break

        down = 0
        for temp_y in range(y+1, h):
            down += 1
            if trees[temp_y][x] >= trees[y][x]:
                break

        left = 0
        for temp_x in range(x, 0, -1):
            left += 1
            if trees[y][temp_x-1] >= trees[y][x]:
                break

        up = 0
        for temp_y in range(y, 0, -1):
            up += 1
            if trees[temp_y-1][x] >= trees[y][x]:
                break

        highest_score = max(highest_score, left*right*up*down)

print('part 2:', highest_score)
# print(highest_score == 8)
