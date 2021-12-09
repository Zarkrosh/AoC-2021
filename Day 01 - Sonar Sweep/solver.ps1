# Advent of Code 2021
# Day 1

Filter Get-DepthIncreases {
	If ($_ -gt 0) {
		$_
	}
}

function Invoke-SolvePart1 {
	param (
		$data
	)

	$changes = @()
	$prev = $data[0]
	foreach($depth in $data) {
		$changes += ($depth - $prev)
		$prev = $depth
	}

	$($changes | Get-DepthIncreases).Length
}

function Invoke-SolvePart2 {
	param (
		$data
	)

	$changes = @()
	$prev = $data[0]
	foreach($depth in $data) {
		$changes += ($depth - $prev)
		$prev = $depth
	}

	$($changes | Get-DepthIncreases).Length
}


$inputTest = Get-Content -LiteralPath test.txt
$inputChall = Get-Content -LiteralPath input.txt


########################
######## PART 1 ########
########################
# TEST
$testPart1 = Invoke-SolvePart1 -data $inputTest
if ($testPart1 -ne 7) {
	Write-Output "[!] Part 1: Test failed. Got result: $testPart1"
	exit
}
# CHALLENGE
Write-Output "[*] Part 1: $(Invoke-SolvePart1 -data $inputChall)"


########################
######## PART 2 ########
########################
# TEST
$testPart2 = Invoke-SolvePart2 -data $inputTest
if ($testPart2 -ne 5) {
	Write-Output "[!] Part 2: Test failed. Got result: $testPart1"
	exit
}
# CHALLENGE
Write-Output "[*] Part 2: $(Invoke-SolvePart2 -data $inputChall)"