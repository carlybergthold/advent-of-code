# Part One
for x in numbers:
    for y in numbers:
      if x + y == 2020:
        print(x, y)


# Part Two
for x in numbers:
    for y in numbers:
      for z in numbers:
        if x + y + z == 2020:
          print(x, y, z)