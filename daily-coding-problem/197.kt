/**
Given an array and a number k that's smaller than the length of the array, 
rotate the array to the right k elements in-place.
 */

// run with https://pl.kotl.in/8QpmNwvzy


fun main() {

    fun rotateArr(arr: List<Any>, k: Int): List<Any> {
        val length = arr.size
        val endKElements = arr.slice(k..length-1)
        val startingElements = arr.slice(0..k-1)
        return endKElements + startingElements
    }

    var l = listOf(1, 2, 3, 4, 5, 6)
    var k = 2
    println(rotateArr(l, k))
}