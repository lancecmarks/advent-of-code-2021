# Using readlines()
file1 = open('depth-input.txt', 'r')
Lines = file1.readlines()
 
prev = None
increase = 0
# Strips the newline character
for line in Lines:
    if prev == None:
        prev = int(line)
    else:
        dif = int(line) - prev
        prev = int(line)
        if dif > 0:
            increase += 1


print("Total increases is {}".format(increase))