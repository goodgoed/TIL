// /**
//  * @param {number[][]} matrix
//  * @return {number[]}
//  */
// var spiralOrder = function (matrix) {
//     let columnStart = 0;
//     let columnFinish = matrix[0].length - 1;
//     let rowStart = 0;
//     let rowFinish = matrix.length - 1;
//     const totalSpiralTime = matrix.length - 1;

//     let counter = 0;
//     const ret = [];
//     while (counter <= totalSpiralTime) {
//       for (let i = columnStart; i <= columnFinish; i++) {
//         ret.push(matrix[rowStart][i]);
//       }

//       for (let i = rowStart + 1; i <= rowFinish; i++) {
//         ret.push(matrix[i][columnFinish]);
//       }

//       if (rowStart !== rowFinish && columnStart !== columnFinish) {
//         for (let i = columnFinish - 1; i >= columnStart; i--) {
//           ret.push(matrix[rowFinish][i]);
//         }

//         for (let i = rowFinish - 1; i > rowStart; i--) {
//           ret.push(matrix[i][columnStart]);
//         }
//       }

//       counter++;
//       columnStart++;
//       columnFinish--;
//       rowStart++;
//       rowFinish--;
//     }

//     return ret;
//   };

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  let columnStart = 0;
  let columnFinish = matrix[0].length - 1;
  let rowStart = 0;
  let rowFinish = matrix.length - 1;

  const ret = [];
  while (columnStart <= columnFinish && rowStart <= rowFinish) {
    for (let i = columnStart; i <= columnFinish; i++) {
      ret.push(matrix[rowStart][i]);
    }
    rowStart++;

    for (let i = rowStart; i <= rowFinish; i++) {
      ret.push(matrix[i][columnFinish]);
    }
    columnFinish--;

    if (rowStart <= rowFinish) {
      for (let i = columnFinish; i >= columnStart; i--) {
        ret.push(matrix[rowFinish][i]);
      }
      rowFinish--;
    }

    if (columnStart <= columnFinish) {
      for (let i = rowFinish; i >= rowStart; i--) {
        ret.push(matrix[i][columnStart]);
      }
      columnStart++;
    }
  }

  return ret;
};

const test1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
const test2 = [[7], [9], [6]];
const test3 = [[1]];
const test4 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
];
const test5 = [
  [2, 5, 8],
  [4, 0, -1],
];

console.log(spiralOrder(test4));
