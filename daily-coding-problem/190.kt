/**
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
 */

// run with https://pl.kotl.in/m0bOCU4uQ
// almost...

import kotlin.math.*

fun main() {

    fun maxSubArray(arr: List<Int>): Int {
        // bump out of empty array
        if (arr.isEmpty()) {
            return 0
        }

        var currSubArray = mutableListOf<Int>()
        var maxSum = -999 // arbitraily low number (change to negative inf)

        var atStart = true
        var startingSubArray = emptyList<Int>()

        arr.forEach { e ->
            currSubArray.add(e)
            val tempSum = currSubArray.sum()

            if (tempSum > maxSum) {
                // set new max
                if (tempSum > e) {
                    maxSum = currSubArray.sum()
                } else {
                    // case where element is greater than the previous sum (negative numbers involved)
                    maxSum = e
                    currSubArray = mutableListOf(e)
                }
            } else {
                // save array if we are at the beginning of the array
                if (atStart) {
                    // do not save if first elements do not match
                    // do not save if starts with negative number
                    if ((currSubArray.first() == arr.first()) and (currSubArray.first() > 0)) {
                        startingSubArray = currSubArray
                    }
                    atStart = false
                }
                // clear
                currSubArray = mutableListOf<Int>()
            }
        }

        // see if end and start can make a greater sub array
        if (currSubArray != startingSubArray) {
            maxSum = max(maxSum, maxSum + startingSubArray.sum())
        }
        return maxSum
    }

    val arr1 = listOf(8, -1, 3, 4)
    val arr2 = listOf(-4, 5, 1, 0)
    val arr3 = listOf(-1, -1, -3)
    val arr4 = listOf(1, 2, 3, 4)
    val arr5 = listOf(1, 2, 3, 4, 0)
    println(maxSubArray(arr1))
    println(maxSubArray(arr2))
    println(maxSubArray(arr3))
    println(maxSubArray(arr4))
    println(maxSubArray(arr5))
}