/*
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
*/

// First thought is to square each element and sort the original list

function squareAndSort(sortedList) {
    return sortedList.map(e => e**2).sort((a, b) => a - b)
}

console.log(squareAndSort([-9, -2, 0, 2, 3]))

// could build a sorted array as you go
// could move negative integers to positive places before squaring
// but why not use the built ins, as they will typically be more efficient 