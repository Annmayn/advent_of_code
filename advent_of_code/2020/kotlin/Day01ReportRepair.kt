import java.io.File

typealias IntList = MutableList<Int>

fun readInput(input_file: String): IntList {
    var dataset: IntList = mutableListOf()
    File(input_file).forEachLine() { dataset.add(it.toInt()) }
    return dataset
}

fun partOne(data: IntList, target: Int): Int {
    var refSet: MutableSet<Int> = mutableSetOf()
    for (each in data) {
        val diff = target - each
        if (refSet.contains(diff)) {
            return each * diff
        }
        refSet.add(each)
    }
    return -1
}

fun partTwo(data: IntList, target: Int): Int {
    for (i in 0 until data.size) {
        val newTarget = target - data[i]
        val tmp = solve(data, newTarget, i + 1)
        if (tmp != -1) {
            return data[i] * tmp
        }
    }
    return -1
}

fun solve(data: IntList, target: Int, ind: Int): Int {
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

fun multList(arr: MutableList<Int>): Int {
    var res = 1
    for (i in arr) {
        res *= i
    }
    return res
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
