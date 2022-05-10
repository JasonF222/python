/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

const str4 = "ti esrever dna ti pilf nwod gnaht ym tup I"
const expected4= "I put my thang down flip it and reverse it"

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.

/* we wanna reverse the letters in the string */
/* Momma, just killed a man*/


function reverseWords(str) {
    /*If you gotta big, let me search ya. */
    let theBoys = " ";
    let words = str.split(" ");
    for(var i = 0; i < words.length; i++ ) {
        theBoys += featuringKelis(words[i]).toString();
    }
    /* to find out how hard I gotta work ya */
    return theBoys.toString();
}
console.log(reverseWords(str4))

/* this is our array.prototype.reverse helper function */
function featuringKelis(ekahsklim) {
    /* Is it worth it? Let me work it. */
    let milkshake = " ";
    for(var i = ekahsklim.length - 1; i >= 0; i--) {
        milkshake += ekahsklim[i];
    }
    /* I put my thang down, flip it, and reverse it */
    return milkshake;
} 

// console.log(missyElliot(str2));
// **********************************************************

/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const two_str1 = "This is a test";
const two_expected1 = "test a is This";

const two_str2 = "hello";
const two_expected2 = "hello";

const two_str3 = "   This  is a   test  ";
const two_expected3 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */


function reverseWordOrder(wordsStr) {
    /*Put that on ya*/
    let theBoys = "";
    let words = mySplit( wordsStr, " " );
    console.log(words)
    for (var i = words.length - 1; i >= 0; i--) {
        if(words[i]) {
            theBoys += words[i] + " ";
        }
    }
    /* see my hips and my tips, don't ya? */
    return theBoys;
}
console.log(reverseWordOrder(two_str3))

function mySplit(str, seperator) {
    let newArr = []
    let temp = ''
    for (const char of str) {
        if (char === seperator) {
            newArr.push(temp)
            temp = ""
        } else {
            temp += char
        }
    }
    newArr.push(temp)
    return newArr
}
