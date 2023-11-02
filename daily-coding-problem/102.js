/*
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9,
then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
*/

// for each element, sum consecutive indices until either equals or exceeds K
// if equals, return sequence
// if exceeds, go to next element and restart

function findContiguousSum(l, K) {
    function sumList(_l) {
        return _l.reduce((partialSum, a) => partialSum + a, 0);
    }
    let ans = [];
    let i = 0;
    // iterate through elements of l
    // for each, walk through remaining elements and sum
    while (l[i]) {
        const nextL = l.slice(i);
        let j = 0;
        while (nextL[j]) {
            ans.push(nextL[j]);
            const sum = sumList(ans);
            if (sum === K) {
                // return sequence if equals
                break;
            } else if (sum > K) {
                // next element if exceeds
                ans = [];
                break;
            }
            j++;
        }
        if (ans.length > 0) {
            break;
        }
        i++;
    }
    // check to make sure sum equals, possible it is less
    // will be [] if no contiguous sequence exists
    return sumList(ans) === K ? ans : []  
}

console.log("expected [2,3,4]", findContiguousSum([1,2,3,4,5], 9))
console.log("expected [5,4]", findContiguousSum([5,4,3,2,1], 9))
console.log("expected []", findContiguousSum([5,4,3,2,1], 11))
console.log("expected [5,3,2,1]", findContiguousSum([4,5,3,2,1], 11))
console.log("expected [3,4]", findContiguousSum([4,5,3,4,1], 7))
console.log("expected []", findContiguousSum([1,1,1,1,1], 7))