with open('7_input.txt', 'r') as f:
    all_lines = f.read().split('\n')

current_path = ''
folders = dict()

for i, current_line in enumerate(all_lines):
    prev_line = ''
    if i > 0:
        prev_line = all_lines[i-1]

    if current_line.startswith('$ cd '):
        destination = current_line.split('$ cd ')[1]
        if destination == '..':
            current_path = ' '.join(current_path.split(' ')[:-1])
        else:
            current_path += f' {destination}'
            if not current_path in folders:
                folders[current_path] = []
        continue

    if current_line.startswith('dir'):
        folders[current_path].append(current_path + ' ' + current_line.split(' ')[1])
        continue

    if current_line.split(' ')[0].isdigit():
        folders[current_path].append(int(current_line.split(' ')[0]))
        continue

# sort so we get the deepest folders first
folders = {key: value for key, value in sorted(folders.items(), key=lambda item: item[0].count(' '), reverse=True)}

folder_sizes = dict()
for key, value in folders.items():
    folder_sizes[key] = 0
    for content in value:
        if isinstance(content, int):
            folder_sizes[key] += content
        elif content in folder_sizes:
            folder_sizes[key] += folder_sizes[content]


folders_under_100000 = {key: value for key, value in folder_sizes.items() if value <= 100_000}
print('part 1 result:', sum(folders_under_100000.values()))

min_space_to_free = 30_000_000 - (70_000_000 - folder_sizes[' /'])
folders = [size for size in folder_sizes.values() if size >= min_space_to_free]
print('part 2 result:', min(folders))
