slope = []
with open('/Users/Carly/workspace/personal/advent-of-code/2020/day-3/input.txt', 'r') as f:
    slope = [(i) for i in f.read().splitlines()]

index = 0
treeCount = 0

for line in slope:
    if index > 30:
        index = abs(index - 31)

    isATree = True if line[index] == "#" else False

    if isATree:
        treeCount += 1

    index = index + 3

print(treeCount)