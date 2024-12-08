/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findBall = function (grid) {
  const res = Array(grid[0].length);

  for (let index = 0; index < grid[0].length; index++) {
    res[index] = findBallPosition(0, index, grid);
  }

  return res;
};

var findBallPosition = function (row, currentPosition, grid) {
  if (row === grid.length) return currentPosition;

  if (grid[row][currentPosition] === 1) {
    if (
      currentPosition !== grid[0].length &&
      grid[row][currentPosition + 1] === 1
    ) {
      return findBallPosition(row + 1, currentPosition + 1, grid);
    } else {
      return -1;
    }
  }
  if (grid[row][currentPosition] === -1) {
    if (currentPosition !== 0 && grid[row][currentPosition - 1] === -1) {
      return findBallPosition(row + 1, currentPosition - 1, grid);
    } else {
      return -1;
    }
  }
};

const grid = [
  [1, 1, 1, -1, -1],
  [1, 1, 1, -1, -1],
  [-1, -1, -1, 1, 1],
  [1, 1, 1, 1, -1],
  [-1, -1, -1, -1, -1],
];

const res = findBall(grid);

console.log(res);
