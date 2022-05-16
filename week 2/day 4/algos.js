/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";

const rotateAmnt6 = 5;
const expected6 = "WorldHello ";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */

/* new string to push into as rotating */
/* what do we do to set amnt to be less than str.length when difference is greater than str.length */


function rotateStr(str, amnt) {

    let bucket = "";

    if (amnt > str.length){
        amnt = amnt % str.length;
    }
    for(let j = str.length - amnt;j < str.length; j++){
        bucket += str[j];
    }

    for(let i = 0; i < str.length - amnt; i++) {
        bucket += str[i];
    }
    return bucket;
}
console.log(rotateStr(str, 1));
console.log(rotateStr(str, 2));
console.log(rotateStr(str, 4));
console.log(rotateStr(str, 13));
console.log(rotateStr(str, 5));





/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const two_strA1 = "ABCD";
const two_strB1 = "CDAB";
// CDAB -> BCDA -> ABCD
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const two_expected1 = true;

const two_strA2 = "ABCD";
const two_strB2 = "CDBA";
// CDBA -> ACDB -> BACD -> DBAC -> CDBA
// Explanation: all same letters in 2nd string, but out of order
const two_expected2 = false;

const two_strA3 = "ABCD";
const two_strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const two_expected3 = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */




function isRotation(s1, s2) {
    for (let i = 0; i < s2.length; i++) {
        let mover = rotateStr(s2, i);
        if (mover == s1) {
            return true;
        }
        else false;
    }
}
console.log(isRotation(two_strA1, two_strB1));
console.log(isRotation(two_strA2, two_strB2));
console.log(isRotation(two_strA3, two_strB3));