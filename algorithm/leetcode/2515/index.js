/**
 * @param {string[]} words
 * @param {string} target
 * @param {number} startIndex
 * @return {number}
 */
var closetTarget = function (words, target, startIndex) {
  //start searching from startIndex
  //search through left and right
  //search until left and right have the same string

  //1st solution
  //   if (words[startIndex] === target) {
  //     return 0;
  //   }

  //   let res = 1;
  //   let n = words.length;
  //   for (
  //     let i = 1;
  //     words[(startIndex - i + n) % n] !== words[(startIndex + i) % n];
  //     i++
  //   ) {
  //     let left = words[(startIndex - i + n) % n];
  //     let right = words[(startIndex + i) % n];

  //     if (left === target || right === target) return res;

  //     res++;
  //   }

  //   return -1;

  /** failed at:
   * ["rxkwbvfjgi","rxkwbvfjgi","axwkycunjp","eupyslvhvv","pquwrrbxbz","rxkwbvfjgi","hbkhlksdbx","neyibobjnz","axwkycunjp","eupyslvhvv"]
   * "pquwrrbxbz"
   * 8
   * output: -1
   */

  //search to the right first and record
  //search to the left and record
  // return the lower number

  //2nd solution
  if (words[startIndex] === target) {
    return 0;
  }

  let right_res = 1;
  let n = words.length;
  for (let i = startIndex; startIndex !== (i + 1) % n; i++) {
    let index = (i + 1) % n;
    if (words[index] === target) break;
    right_res++;
  }

  let left_res = 1;
  for (let i = startIndex; startIndex !== (i - 1 + n) % n; i--) {
    let index = (i - 1 + n) % n;
    if (words[index] === target) {
      return Math.min(right_res, left_res);
    }
    left_res++;
  }

  return -1;

  // Difficulty
  // Figuring out when to stop searching
};

console.log(
  closetTarget(
    [
      "rxkwbvfjgi",
      "rxkwbvfjgi",
      "axwkycunjp",
      "eupyslvhvv",
      "pquwrrbxbz",
      "rxkwbvfjgi",
      "hbkhlksdbx",
      "neyibobjnz",
      "axwkycunjp",
      "eupyslvhvv",
    ],
    "pquwrrbxbz",
    8
  )
);
