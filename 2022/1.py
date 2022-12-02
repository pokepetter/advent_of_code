with open('1_input.txt', 'r') as f:
    bags = [[int(e) for e in bag.split('\n') if e] for bag in f.read().split('\n\n')] # convert each paragraph to a list of numbers
    bags = [sum(e) for e in bags]
    bags.sort(reverse=True)

    print(f'the biggest bag has {bags[0]} kcal')

    sum_of_three_biggest_bags = sum(bags[:3])
    print(f'the three biggest bag has a total of {sum_of_three_biggest_bags} kcal')
