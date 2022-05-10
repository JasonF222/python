/* 
Given an array of strings
return the number of times each string occurs (a frequency / hash table)
*/

// const arr1 = ["a", "a", "a"];
// const expected1 = {
    //   a: 3,
    // };

const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */


/* make empty object { }
if no key in object, add key to object
compare indicies to key
if match, += 1 to key value
otherwise continue iterating
newObj.hasOwnProperty(arr[i]) */





function makeFrequencyTable(arr) {
    let newObj = { };
    for(var i = 0; i < arr.length; i++) {
        if( arr[i] in newObj) {
            newObj[arr[i]] += 1;
        }
        else {
            newObj[arr[i]] = 1;
        }
    }
    return newObj;
}

console.log(makeFrequencyTable(arr3))

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const two_nums1 = [1];
const two_expected1 = 1;

const two_nums2 = [5, 4, 5];
const two_expected2 = 4;

const two_nums3 = [5, 4, 3, 4, 3, 4, 5];
const two_expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const two_nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const two_expected4 = 1;



function oddOccurrencesInArray(nums) {
    let counts = makeFrequencyTable(nums);
    /* we now have an object with key val pairs of each number and how many times it shows up */
    for(let key in counts) {
        if(counts[key] %2 != 0) {
            return key;
        }
    }
}

console.log(oddOccurrencesInArray(two_nums4))