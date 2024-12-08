/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  //1st solution
    if (nums.length > 2) {
      let res = [];
      for (let i = 0; i < nums.length; i++) {
        if (res.length > 0) res = [];
        res.push(i);
        for (let j = 0; j < nums.length; j++) {
          if (i === j) continue;
          if (nums[i] + nums[j] === target) {
            res.push(j);
            return res;
          }
        }
      }
    }
    return [0, 1];
    }

  //   return [0, 1];

  //2nd solution
  //   if (nums.length > 2) {
  //     const hashMap = new Map();
  //     let res = [];
  //     for (let index = 0; index < nums.length; index++) {
  //       hashMap.set(nums[index], index);
  //     }

  //     for (let index = 0; index < nums.length; index++) {
  //       if (res.length > 0) res = [];
  //       res.push(index);

  //       const testIndex = hashMap.get(target - nums[index]);
  //       if (testIndex !== undefined && testIndex !== index) {
  //         res.push(testIndex);
  //         return res;
  //       }
  //     }
  //   }
  //   return [0, 1];

  //3rd solution
  if (nums.length > 2) {
    const hashMap = new Map();
    const res = new Array(2);
    for (let index = 0; index < nums.length; index++) {
      hashMap.set(nums[index], index);
    }

    for (let index = 0; index < nums.length; index++) {
      res[0] = index;

      const testIndex = hashMap.get(target - nums[index]);
      if (testIndex !== undefined && testIndex !== index) {
        res[1] = testIndex;
        return res;
      }
    }
  }
  return [0, 1];
};

class testRunner {
  constructor(nums, target, expectedRes) {
    this.nums = nums;
    this.target = target;
    this.expectedRes = expectedRes;
  }

  result() {
    const testRes = twoSum(this.nums, this.target);
    for (let index = 0; index < this.expectedRes.length; index++) {
      if (this.expectedRes[index] !== testRes[index]) return false;
    }
    return true;
  }
}

console.log(new testRunner([1, 2], 3, [0, 1]).result());
console.log(new testRunner([2, 7, 11, 15], 9, [0, 1]).result());
console.log(new testRunner([3, 2, 4], 6, [1, 2]).result());
console.log(new testRunner([2, 5, 5, 11], 10, [1, 2]).result());
