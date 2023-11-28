/*
Given a mapping of digits to letters (as in a phone number),
and a digit string,
return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …}
then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
*/

// for each letter in the number mapping add each letter from the mapping of the next number
// do this recursively

const MAPPING = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    // ...
}

function getAllLetters(numString) {
    let ans = [];
    
    numString.split("").forEach(num => {
        const tempAns = ans.slice()
        if (tempAns.length) {
            ans = [];
            MAPPING[num].forEach(letter => {
                tempAns.forEach(a => {
                    ans.push(a+letter);
                })
            })
        } else {
            ans = MAPPING[num]
        }
    })
    ans.sort() // for convenience
    return ans
}

console.log(getAllLetters("23"))
console.log(getAllLetters("243"))