#!/usr/bin/python3
# Advent of Code 2021
# Day 2

class Submarine:
    def __init__(self, correctlyDriven) -> None:
        self.x = 0
        self.depth = 0
        self.aim = 0
        self.correctlyDriven = correctlyDriven
    
    def move(self, course) -> None:
        for command in course:
            dir, val = command.split(" ")
            val = int(val)
            if dir == "forward":
                self.x += val
                if self.correctlyDriven:
                    self.depth += self.aim * val
            elif dir == "down":
                if self.correctlyDriven:
                    self.aim += val
                else:
                    self.depth += val
            elif dir == "up":
                if self.correctlyDriven:
                    self.aim -= val
                else:
                    self.depth -= val


def readInput(file):
    with open(file, "r") as inp:
        return [l.strip() for l in inp.readlines()]

def solveFirstPart(data) -> int:
    submarine = Submarine(correctlyDriven=False)
    submarine.move(data)
    return submarine.x * submarine.depth

def solveSecondPart(data) -> int:
    submarine = Submarine(correctlyDriven=True)
    submarine.move(data)
    return submarine.x * submarine.depth


courseTest = readInput("test.txt")
course = readInput("input.txt")

# TEST
assert solveFirstPart(courseTest) == 150
# CHALLENGE
print("[*] Part 1: {}".format(solveFirstPart(course)))

# TEST
assert solveSecondPart(courseTest) == 900
# CHALLENGE
print("[*] Part 2: {}".format(solveSecondPart(course)))