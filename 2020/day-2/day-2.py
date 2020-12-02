passwords = []
with open('input.txt', 'r') as f: # Read in the data as a list of ints
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
    print("there are ", counter, letter, "in ", password)

    for i in range(beginningRange, endingRange):
        if i == counter:
            correctPasswordCount += 1

# print(correctPasswordCount, len(passwords))