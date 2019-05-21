// 5/7/19

// Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
//
// For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
//
// As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
//
// If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

function convertFrac(lst){
  const denoms = lst.map(pair => pair[1])
  let check = Math.max(...denoms)
  if (denoms.length) {
    while (check <= denoms.reduce((a, b) => a*b)) {
      if (denoms.every(num => check % num === 0)) { return lst.map(pair => `(${(check / pair[1])*pair[0]},${check})`).join('') }
      check++
    }
  }
  return ''
}
