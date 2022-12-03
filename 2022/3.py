with open('3_input.txt', 'r') as f:
    all_bags = f.read().split('\n')

sum = 0

for bag in all_bags:
    count = len(bag)
    first_part, second_part = bag[:count//2], bag[count//2:]
    # print(first_part, second_part)
    common_items = [e for e in first_part if e in second_part]
    if not common_items:
        continue

    # print(common_items)
    sum += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(common_items[0]) + 1


print(sum)


# part 2
bags_in_groups_of_three = [[all_bags[i+j] for j in range(3)] for i in range(0, len(all_bags)-3, 3)]
# print(bags_in_groups_of_three)
sum = 0

for group in bags_in_groups_of_three:
    common_items = [e for e in group[0] if e in group[1] and e in group[2]]
    # print(common_items)
    sum += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(common_items[0]) + 1

print(sum)
