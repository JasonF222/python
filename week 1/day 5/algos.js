// /* 
//   Zip Arrays into Map
  
  
//   Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
//   Associative arrays are sometimes called maps because a key (string) maps to a value 
//  */

//   const keys1 = ["abc", 3, "yo"];
//   const vals1 = [42, "wassup", true];
//   const expected1 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
//   };

//   const keys3 = ["abc", 3, "yo", "something"];
//   const vals3 = [42, "wassup", true];
//   const expected3 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
//     something: ''
//   };

//   const keys4 = ["abc", 3, "yo"];
//   const vals4 = [42, "wassup", true, "something"];
//   const expected4 = false
  
//   const keys2 = [];
//   const vals2 = [];
//   const expected2 = {};
  
  /**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */

// const keys1 = ["abc", 3, "yo"];
// const vals1 = [42, "wassup", true];
// const expected1 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
// };

// output =  [abc: '42', 3: 'wassup', yo: true] //
// keys1[i].push(output)
// val[i] = output[keys[i]]

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true, "something"];

function zipArraysIntoMap(keys, vals) {
    if(vals.length > keys.length) return false;
    var obj = {};
    for (var i = 0; i < keys.length; i++) {
        if (!vals[i]) {
            vals[i] = "";
        }
        // else if (!keys[i]) {
        //     return false;
        // }
        obj[keys[i]] = vals[i];
    }
    return obj;
}

console.log(zipArraysIntoMap(keys1, vals1))















  /* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

// const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
// const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

// // bonus
// const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something:["thing1", "thing2"] };
// const two_expected2 = { Zaphod: "name", high: "charm", dicey: "morals", thing1:"something", thing2:"something"  };

// const two_obj3 = { name: "Zaphod", charm: "high", morals: "dicey", something:"dicey"  };
// const two_expected3 = { Zaphod: "name", high: "charm", dicey: ["morals", "something"]  };

// /**
//  * Inverts the given object's key value pairs so that the original values
//  * become the keys and the original keys become the values.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Object<string, any>} obj
//  * @return The given object with key value pairs inverted.
//  */

// // set vals of obj1 to equal keys of result, and keys of obj1 to be vals of result //

// // const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
// // const two_obj1_result ={Zaphod: "name", high: "charm", dicey: "morals"}

// // const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };

// // function invertObj(obj) {
// //     var obj = {};
// //     var vals = key;
// //     var keys = 
// //     for (var i = 0; i <= obj.length; i++) {
// //         if (!vals[i]) {
// //             vals[i] = "";
// //         }
// //         else if (!keys[i]) {
// //             return false;
// //         }
// //         obj[vals[i]] = keys[i];
// //     }
// //     return obj;
// // }
// // console.log(invertObj(two_obj1))