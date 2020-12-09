import math

boardingPasses = []
with open('/Users/Carly/workspace/personal/advent-of-code/2020/day-5/input.txt', 'r') as f:
    boardingPasses = [(i) for i in f.read().splitlines()]


boardingPass = "FBFBBFFRLR"

for index, char in enumerate(boardingPass):
    print(index, char)

    if index == 0:
        frontHalf = True if boardingPass[0] == "F" else False
        possibleRows = [0,63] if frontHalf else [64,127]

    if 1 <= index <= 6:
        frontHalf = True if char[index] == "F" else False
        half = (possibleRows[1] - possibleRows[0]) / 2

        if frontHalf:
            possibleRows = [possibleRows[0], math.floor(half)]
        else:
            possibleRows = [math.ceil(half), possibleRows[1]]
    print(possibleRows)

    # leftHalf = True if boardingPass[7] == "L" else False
    # possibleSeats = [0,3] if leftHalf else [4,7]

    # leftHalf = True if boardingPass[8] == "L" else False
    # if leftHalf:
    #     possibleSeats = [0,1] if possibleSeats == [0,3] else [4,5]
    # else:
    #     possibleSeats = [4,5] if possibleSeats == [4,7] else [6,7]

    # leftHalf = True if boardingPass[9] == "L" else False
    # seat = possibleSeats[0] if leftHalf else possibleSeats[1]
    # print(seat)

    # uniqueId = row * 8 + seat
    # print(uniqueId)





