#!/usr/bin/python3
# Advent of Code 2021
# Day 4

import numpy as np
from typing import List


class BingoBoard:
    def __init__(self, numberMatrix) -> None:
        self.numberMatrix = numberMatrix
        self.marks = np.zeros((len(numberMatrix), len(numberMatrix[0])), dtype=bool)
    
    def mark(self, number) -> None:
        for i in range(len(self.numberMatrix)):
            row = self.numberMatrix[i]
            if number in row:
                self.marks[i][row.index(number)] = True
                break

    def isWinner(self) -> bool:
        # Rows check
        for row in self.marks:
            if all(row):
                return True
        # Columns check
        for col in [[row[i] for row in self.marks] for i in range(len(self.marks[0]))]:
            if all(col):
                return True

    def getWinningScore(self, lastNumber) -> int:
        res = 0
        for i in range(len(self.numberMatrix)):
            for j in range(len(self.numberMatrix[0])):
                if not self.marks[i][j]:
                    res += self.numberMatrix[i][j]
        return res * lastNumber


def readInput(file):
    with open(file, "r") as f:
        drawnNumbers = [int(n) for n in f.readline().strip().split(',')]
        lines = [s.strip() for s in f.readlines()]

        boards = []
        tempMatrix = None
        for line in lines:
            if len(line) == 0:
                # New board definition
                if tempMatrix != None:
                    boards.append(BingoBoard(tempMatrix))
                tempMatrix = []
            else:
                tempMatrix.append([int(n) for n in line.split()])
        boards.append(BingoBoard(tempMatrix)) # Last one
        return drawnNumbers, boards

def solveFirstPart(drawnNumbers: List[int], boards: List[BingoBoard]) -> int:
    for number in drawnNumbers:
        for board in boards:
            board.mark(number)
            if board.isWinner():
                return board.getWinningScore(number)
    return None

def solveSecondPart(drawnNumbers: List[int], boards: List[BingoBoard]) -> int:
    for number in drawnNumbers:
        for board in boards:
            board.mark(number)
        nBoards = [b for b in boards if not b.isWinner()]
        if len(nBoards) == 0:
            return boards[0].getWinningScore(number)
        else:
            boards = nBoards
    return None


drawnNumbersTest, boardsTest = readInput("test.txt")
drawnNumbers, boards = readInput("input.txt")

# TEST
assert solveFirstPart(drawnNumbersTest, boardsTest) == 4512
# CHALLENGE
print("[*] Part 1: {}".format(solveFirstPart(drawnNumbers, boards)))


drawnNumbersTest, boardsTest = readInput("test.txt")
drawnNumbers, boards = readInput("input.txt")

# TEST
assert solveSecondPart(drawnNumbersTest, boardsTest) == 1924
# CHALLENGE
print("[*] Part 2: {}".format(solveSecondPart(drawnNumbers, boards)))