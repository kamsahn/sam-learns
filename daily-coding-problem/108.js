/*
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
*/

// find begining of one string in the other
// "shift" by slicing
// compare strings

function shiftedStrings(stringA, stringB) {
    if (stringA.includes(stringB[0])) {
        const startIndex = stringA.indexOf(stringB[0])
        const end = stringA.substring(0, startIndex)
        const start = stringA.substring(startIndex)
        const shiftedStringA = start + end
        return shiftedStringA === stringB
    }
    return false
}

console.log("abcde can shift to cdeab", shiftedStrings("abcde", "cdeab"))
console.log("abcde can shift to cedab", shiftedStrings("abcde", "cedab"))
console.log("12345 can shift to 12346", shiftedStrings("12345", "12346"))
console.log("12345 can shift to 1234", shiftedStrings("12345", "1234"))
console.log("12345 can shift to 5123", shiftedStrings("12345", "5123"))
console.log("12345 can shift to 51234", shiftedStrings("12345", "51234"))