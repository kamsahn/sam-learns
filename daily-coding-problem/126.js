/*
This problem was asked by Facebook.

Write a function that rotates a list by k elements. 
For example, [1, 2, 3, 4, 5, 6] 
rotated by two becomes [3, 4, 5, 6, 1, 2]. 
Try solving this without creating a copy of the list. 

How many swap or move operations do you need?
*/

/*
first thought is to change each element in the array from value and index i to value and index i + k
this would be n opterations where n is the length of the array

alternatively, one could move the first k elements to the end of the array
this would b k operations
*/

function rotateArray (arr, k) {
  if (arr.length === k) {
    return arr
  }

  const tempArr = [];

  while (tempArr.length < k) {
    tempArr.push(arr.shift());
  }

  while (tempArr.length > 0) {
    arr.push(tempArr.shift());
  }
  return arr
}

const arr = [1, 2, 3, 4, 5, 6];
// console.log(arr)
// console.log("rotate array by two")
// console.log(rotateArray(arr, 2))

// turns out, this solution is 2k

function rotateArrayNew(arr, k) {
  if (arr.length === k) {
    return arr
  }

  let i = 0
  while (i < k) {
    arr.push(arr.shift())
    i++
  }
  return arr
}

console.log(rotateArrayNew(arr, 2))
// this solution takes k operations