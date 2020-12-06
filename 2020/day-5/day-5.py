import os

slope = []
with open('/Users/Carly/workspace/personal/advent-of-code/2020/day-5/input.txt', 'r') as f:
    slope = [(i) for i in f.read().splitlines()]

print(slope)