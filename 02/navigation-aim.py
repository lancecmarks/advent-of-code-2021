file = open("movement.txt", "r")

line_count = 0

depth = 0
horizontal = 0
aim = 0

for line in file:
    parts = line.strip().split(' ')
    direction = parts[0]
    quantity = int(parts[1])

    if direction == 'forward':
        horizontal += quantity
        depth += (aim * quantity)
    if direction == 'down':
        aim += quantity
    if direction == 'up':
        aim -= quantity

file.close()

print('Depth is {} and Horizontal is {}\n'.format(depth, horizontal))