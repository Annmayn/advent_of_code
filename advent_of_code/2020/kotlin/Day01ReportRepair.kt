package day1

import java.io.File

typealias IntList = List<Int>

fun readInput(input_file: String): IntList {
    return File(input_file).readLines().map { it.toInt() }
}

fun partOne(data: IntList, target: Int, ind: Int = 0): Int {
    var refSet: MutableSet<Int> = mutableSetOf()
    for (i in ind until data.size) {
        val diff = target - data[i]
        if (refSet.contains(diff)) {
            return data[i] * diff
        }
        refSet.add(data[i])
    }
    return -1
}

fun partTwo(data: IntList, target: Int): Int {
    for (i in 0 until data.size) {
        val newTarget = target - data[i]
        val tmp = partOne(data, newTarget, i + 1)
        if (tmp != -1) {
            return data[i] * tmp
        }
    }
    return -1
}

fun main() {
    val input_file = "input/day_1.txt"
    val data = readInput(input_file)
    val target = 2020

    val partOneRes = partOne(data, target)
    println("part one res => $partOneRes")

    val partTwoRes = partTwo(data, target)
    println("part two res => $partTwoRes")
}
