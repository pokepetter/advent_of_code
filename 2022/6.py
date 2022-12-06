with open('6_input.txt', 'r') as f:
    text = f.read()

def find_marker_with_length(n):
    for i in range(0, len(text)-n):
        if len(set(text[i:i+n])) == n:
            break

    return i + n

print(find_marker_with_length(4))
print(find_marker_with_length(14))
