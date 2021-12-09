#!/usr/bin/python3
# Advent of Code 2021
# Day 3

def readInput(file):
    with open(file, "r") as inp:
        return [l.strip() for l in inp.readlines()]

def solveFirstPart(data) -> int:
    gammaRate = ""
    epsilonRate = ""
    length = len(data)
    lengthItem = len(data[0])
    for i in range(lengthItem):
        nOnes = "".join(s[i] for s in data).count('1')
        if nOnes > length/2:
            gammaRate += "1"
            epsilonRate += "0"
        else:
            gammaRate += "0"
            epsilonRate += "1"
    return int(gammaRate, 2) * int(epsilonRate, 2)

def solveSecondPart(data) -> int:
    oxygenGeneratorOptions = data
    co2ScrubberOptions = data

    lengthItem = len(data[0])
    for i in range(lengthItem):
        # Oxygen
        if len(oxygenGeneratorOptions) > 1:
            nOnes = "".join(s[i] for s in oxygenGeneratorOptions).count('1')
            mostCommon = "1" if nOnes >= len(oxygenGeneratorOptions)/2 else "0"
            oxygenGeneratorOptions = list(filter(lambda x: x[i] == mostCommon, oxygenGeneratorOptions))
        # CO2
        if len(co2ScrubberOptions) > 1:
            nOnes = "".join(s[i] for s in co2ScrubberOptions).count('1')
            leastCommon = "0" if nOnes >= len(co2ScrubberOptions)/2 else "1"
            co2ScrubberOptions = list(filter(lambda x: x[i] == leastCommon, co2ScrubberOptions))

    assert len(oxygenGeneratorOptions) == 1
    assert len(co2ScrubberOptions) == 1
    return int(oxygenGeneratorOptions[0], 2) * int(co2ScrubberOptions[0], 2)


inputTest = readInput("test.txt")
inputData = readInput("input.txt")

# TEST
assert solveFirstPart(inputTest) == 198
# CHALLENGE
print("[*] Part 1: {}".format(solveFirstPart(inputData)))


# TEST
assert solveSecondPart(inputTest) == 230
# CHALLENGE
print("[*] Part 2: {}".format(solveSecondPart(inputData)))