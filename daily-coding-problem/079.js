/*
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
*/

// read through the whole array
// if non descending only one time, return true

function oneOffNonDecreaseing(a) {
    let count = 0;
    let prob;
    a.forEach((e, i) => {
        if (e > a[i+1]) {
            prob = i;
            count++;
        }
        
    })
    
    // check for nearly flat arrays (e.g. 4, 4, 4, 3, 3)
    if (count === 1) {
        // change problem element to value before it
        // in case of problem element at i=0, change to value after it
        a[prob] = a[prob === 0 ? prob+1 : prob-1];
        // run through a second time
        a.forEach((e, i) => {
            if (e > a[i+1]) {
                count++
            }
        })
    }
    return count < 2
}

console.log("expected true", oneOffNonDecreaseing([10, 5, 7]))
console.log("expected false", oneOffNonDecreaseing([10, 5, 1]))
console.log("expected true", oneOffNonDecreaseing([4, 5, 11, 6, 8]))
console.log("expected true", oneOffNonDecreaseing([4, 4, 4, 4, 4]))
console.log("expected false", oneOffNonDecreaseing([4, 4, 4, 3, 3]))
console.log("expected false", oneOffNonDecreaseing([4, 4, 3, 3, 3]))
console.log("expected true", oneOffNonDecreaseing([5, 4, 4, 4, 4]))
console.log("expected false", oneOffNonDecreaseing([5, 5, 4, 4, 4, 3, 3]))