var findPosition = function (row, position) {
  let prev = 0;
  let newPosition = [...position];
  for (let index = 0; index < row.length; index++) {
    if (prev === 1 && row[index] === 1) {
      const check = position.findIndex((element) => element === index - 1);
      if (check > -1) {
        newPosition[check] += 1;
      }
    }
    if (prev === -1 && row[index] === -1) {
      const check = position.findIndex((element) => element === index);
      if (check > -1) {
        newPosition[check] -= 1;
      }
    }
    if (row[0] === -1) {
      const check = position.findIndex((element) => element === 0);
      if (check > -1) {
        newPosition[check] = -1;
      }
    }
    if (row[row.length - 1] === 1) {
      const check = position.findIndex((element) => element === row.length - 1);
      if (check > -1) {
        newPosition[check] = -1;
      }
    }
    if (prev === 1 && row[index] === -1) {
      const check1 = position.findIndex((element) => element === index - 1);
      const check2 = position.findIndex((element) => element === index);
      if (check1 > -1) newPosition[check1] = -1;
      if (check2 > -1) newPosition[check2] = -1;
    }

    prev = row[index];
  }

  return newPosition;
};

/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findBall = function (grid) {
  const colLength = grid[0].length;
  const rowLength = grid.length;
  let res = [];

  for (let index = 0; index < colLength; index++) {
    res.push(index);
  }

  for (let index = 0; index < rowLength; index++) {
    res = findPosition(grid[index], res);
  }

  return res;
};

const grid = [
  [1, 1, 1, 1, 1, 1],
  [-1, -1, -1, -1, -1, -1],
  [1, 1, 1, 1, 1, 1],
  [-1, -1, -1, -1, -1, -1],
];

const res = findBall(grid);

console.log(res);
