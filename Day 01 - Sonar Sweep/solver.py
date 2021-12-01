#!/usr/bin/python3
# Advent of Code 2021
# Day 1

def solveFirstPart(data):
    changes = []
    prev = data[0]
    for depth in data[1:]:
        changes.append(depth - prev)
        prev = depth
    return len(list(filter(lambda x: (x > 0), changes)))

def solveSecondPart(data):
    changes = []
    prev = sum(data[0:3])
    for i in range(len(data) - 2):
        window = sum(data[i:i+3])
        changes.append(window - prev)
        prev = window
    return len(list(filter(lambda x: (x > 0), changes)))


# Test input
with open("test.txt", "r") as inp:
    depthsTest = [int(s) for s in inp.readlines()]
# Challenge input
with open("input.txt", "r") as inp:
    depths = [int(s) for s in inp.readlines()]


########################
######## PART 1 ########
########################
# TEST
assert solveFirstPart(depthsTest) == 7

# CHALLENGE
print("[*] Part 1: {}".format(solveFirstPart(depths)))


########################
######## PART 2 ########
########################
# TEST
assert solveSecondPart(depthsTest) == 5

# CHALLENGE
print("[*] Part 2: {}".format(solveSecondPart(depths)))