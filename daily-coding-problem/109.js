/*
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example,
10101010 should be 01010101.
11100010 should be 11010001.

Bonus: Can you do this in one line?
*/

// use map array prototype with index

function swapper(bitInteger) {
    const asString = String(bitInteger);
    const asArray = asString.split("");
    const swappedArray = asArray.map((elem, i) => {
        if (i % 2) {
            return asArray[i-1]
        } else {
            return asArray[i+1]
        }
    })
    return swappedArray.join("")
}

console.log(swapper(10101010))
console.log(swapper(11100010))
// need to return as 8-bit int
