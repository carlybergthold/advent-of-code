passwords = []
with open('input.txt', 'r') as f:
    passwords = [(i) for i in f.read().splitlines()]

correctPasswordCount = 0

for x in passwords:
    splitArray  = x.split()

    letterRange = splitArray[0].split('-')
    letter = splitArray[1][0]
    password = splitArray[2]

    beginningRange = int(letterRange[0])
    endingRange = int(letterRange[1])

    counter = password.count(letter)

    for i in range(beginningRange, endingRange + 1):
        if i == counter:
            correctPasswordCount += 1

print(correctPasswordCount, len(passwords))