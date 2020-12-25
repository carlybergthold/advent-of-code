boardingPasses = []
with open('/Users/Carly/workspace/personal/advent-of-code/2020/day-5/input.txt', 'r') as f:
    boardingPasses = [(i) for i in f.read().splitlines()]

totals = [128, 64, 32, 16, 8, 4, 2, 8, 4, 2]
rows = [0,127]
seats = [0,7]
highestId = 0

for boardingPass in boardingPasses:
    for index, char in enumerate(boardingPass):
        totalSeatsLeft = totals[index]
        half = totalSeatsLeft / 2

        if boardingPass[index] == "F":
            rows[1] = rows[0] + (half - 1)
        elif boardingPass[index] == "B":
            rows[0] = rows[1] - (half - 1)
        elif boardingPass[index] == "L":
            seats[1] = seats[0] + (half - 1)
        else:
            seats[0] = seats[1] - (half - 1)

    uniqueId = rows[0] * 8 + seats[0]
    if uniqueId > highestId:
        highestId = uniqueId

print(highestId)




