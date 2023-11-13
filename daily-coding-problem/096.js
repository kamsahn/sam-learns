/*
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
*/

// for each element, create a list of all remaining elements recursively
// send a answer list (starts with []) and a list of digits
// remove the element from the list of digits and add to answer list
// recur

function allPermutations(digits) {
    const ans = [];
    function helper(inner_digits, perm, i) {
        console.log(inner_digits)
        perm.push(digits[i % digits.length]);
        const temp = inner_digits.filter((e, idx) => e !== digits[i % digits.length]);
        
        if (temp.length) {
            temp.forEach(_ => helper(temp, perm, i+1))
        } else {
            ans.push(perm)
        }
    }
    digits.forEach((_, i) => helper(digits, [], i))
    console.log(ans)
}

allPermutations([1,2,3])