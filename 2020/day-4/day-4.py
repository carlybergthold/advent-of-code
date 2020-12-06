passports = [[]]
with open('/Users/Carly/workspace/personal/advent-of-code/2020/day-4/input.txt', 'r') as f:
    lines = [i for i in f.read().splitlines()]

pass_count = 0
passports.append([])
for idx, line in enumerate(lines):
    if line:
        passports[pass_count].append(line)
    else:
        pass_count+=1
        passports.append([])

for idx, each in enumerate(passports):
    passports[idx] = ' '.join(each)

validPassports = 0

for string in passports:
    if ("byr" not in string
    or "iyr" not in string
    or "eyr" not in string
    or "hgt" not in string
    or "hcl" not in string
    or "ecl" not in string
    or "pid" not in string):
        print("not enough props!")
    else:
        print(string)
        validPassports += 1

print(validPassports)
