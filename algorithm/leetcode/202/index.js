/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
  const map = new Map();
  while (true) {
    const current = n;
    if (map.get(n) === 1) return false;
    const digits = [];

    while (n !== 0) {
      digits.push(n % 10);
      n = Math.trunc(n / 10);
    }

    let sum = 0;
    digits.forEach((digit) => {
      sum += Math.pow(digit, 2);
    });

    if (sum === 1) return true;

    n = sum;
    map.set(current, 1);
  }
};
