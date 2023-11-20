/*
Implement division of two positive integers without using the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
*/

// add the divisor(?) denominator(?) to iself until it equals or exceeds the numerator
// track iteration i
// if equals return i
// if greater than, return i - 1

// ex: 9 / 2
// 2 + 2 + 2 + 2 + 2 = 10, i = 5
// => 10 > 9
// => i - 1 = 4

function divide(n, d) {
    let i = 1;
    let compare = d;
    while (compare < n) {
        compare += d;
        i++;
    }
    return compare === n ? i : i - 1
}

console.log(divide(10, 2))
console.log(divide(9, 2))
console.log(divide(8, 2))
console.log(divide(1, 1))
console.log(divide(10, 10))
console.log(divide(234, 24))