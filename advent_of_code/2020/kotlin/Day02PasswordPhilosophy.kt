package day2

import java.io.File

fun readInput(inputFile: String): List<String> {
    return File(inputFile).readLines()
}

fun partOne(input: List<String>): Int {
    val regex = Regex("""(\d+)-(\d+)\s+(\w)\:\s+(\w+)""")
    var count = 0
    for (each in input) {
        regex.find(each)?.destructured?.let { (minNumStr, maxNumStr, refChar, refWord) ->
            val minNum = minNumStr.toInt()
            val maxNum = maxNumStr.toInt()
            val countChar = refWord.count { it == refChar.single() }
            if (countChar >= minNum && countChar <= maxNum) count++
        }
    }
    return count
}

fun partTwo(input: List<String>): Int {
    val regex = Regex("""(\d+)-(\d+)\s+(\w)\:\s+(\w+)""")
    var count = 0
    for (each in input) {
        regex.find(each)?.destructured?.let { (startStr, endStr, refChar, refWord) ->
            val start = startStr.toInt() - 1 // 0 indexing
            val end = endStr.toInt() - 1

            val startExists = refWord[start] == refChar.single()
            val endExists = refWord[end] == refChar.single()

            if (startExists xor endExists) count++
        }
    }
    return count
}

fun main() {
    val inputFile = "input/day_2.txt"
    val inputData = readInput(inputFile)

    val partOneRes = partOne(inputData)
    println("part one res => $partOneRes")

    val partTwoRes = partTwo(inputData)
    println("part two res => $partTwoRes")
}
