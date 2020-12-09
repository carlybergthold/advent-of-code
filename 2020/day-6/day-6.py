groups = []
with open('/Users/Carly/workspace/personal/advent-of-code/2020/day-6/input.txt', 'r') as f:
    lines = [(i) for i in f.read().splitlines()]

group_count = 0
groups.append([])
for idx, line in enumerate(lines):
    if line:
        groups[group_count].append(line)
    else:
        group_count+=1
        groups.append([])

for idx, each in enumerate(groups):
    groups[idx] = ''.join(''.join(each))

yesCount = 0

for group in groups:
    yesCount += len(set(group))
