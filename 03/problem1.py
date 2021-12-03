def split(word):
    return [char for char in word]


counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

file = open("data.txt", "r")

line_count = 0
for line in file:
    parts = split(line.strip())
    line_count += 1
    print(len(parts))
    for i in range(len(parts)):
        print('i = {}'.format(i))
        counts[i] = counts[i] + int(parts[i])

file.close()


print('The line count is {}\n'.format(line_count))
print('The array is: ')
print(counts)

gamma_rate = ''
epsilon_rate = ''

for i in range(len(counts)):
    if (counts[i] > line_count/2):
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'
    else:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'

print('gamma_rate is {}'.format(gamma_rate))
print('epsilon_rate is {}'.format(epsilon_rate))
# 349 , 000101011101
# 3746, 111010100010
# 1307354
