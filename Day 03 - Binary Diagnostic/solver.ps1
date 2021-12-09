# Advent of Code 2021
# Day 2

class Submarine {
	[int]$X
	[int]$Depth
	[int]$Aim
	[bool]$CorrectlyDriven

	Submarine([bool]$CorrectlyDriven) {
		$this.X = 0
		$this.Depth = 0
		$this.Aim = 0
		$this.CorrectlyDriven = $CorrectlyDriven;
	}

	[void]Move($course) {
		foreach($command in $course) {
			$direction = $command.Split(" ")[0]
			$value = [int]$command.Split(" ")[1]
			switch ($direction) {
				"forward" {
					$this.X += $value
					if ($this.CorrectlyDriven) {
						$this.Depth += $this.Aim * $value
					}
				}
				"down" {
					if ($this.CorrectlyDriven) {
						$this.Aim += $value
					} else {
						$this.Depth += $value
					}
				}
				"up" {
					if ($this.CorrectlyDriven) {
						$this.Aim -= $value
					} else {
						$this.Depth -= $value
					}
				}
			}
		}
	}
}

function Invoke-SolvePart1 {
	param (
		$data
	)

	$submarine = [Submarine]::new($false)
	$submarine.Move($data)
	$submarine.X * $submarine.Depth
}

function Invoke-SolvePart2 {
	param (
		$data
	)

	$submarine = [Submarine]::new($true)
	$submarine.Move($data)
	$submarine.X * $submarine.Depth
}


$inputTest = Get-Content -LiteralPath test.txt
$inputChall = Get-Content -LiteralPath input.txt

# TEST
$testPart1 = Invoke-SolvePart1 -data $inputTest
if ($testPart1 -ne 150) {
	Write-Output "[!] Part 1: Test failed. Got result: $testPart1"
	exit
}
# CHALLENGE
Write-Output "[*] Part 1: $(Invoke-SolvePart1 -data $inputChall)"

# TEST
$testPart2 = Invoke-SolvePart2 -data $inputTest
if ($testPart2 -ne 900) {
	Write-Output "[!] Part 2: Test failed. Got result: $testPart1"
	exit
}
# CHALLENGE
Write-Output "[*] Part 2: $(Invoke-SolvePart2 -data $inputChall)"