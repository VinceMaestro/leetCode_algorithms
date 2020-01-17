/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
  if (nums == null || nums.length == 0 || target == null) {
    return([-1, -1]);
  }
  var left = 0;
  var right = nums.length - 1;
  while (left < right)
  {
    const mid = Math.floor(left + (right - left) / 2);
    if (nums[mid] > target) {
      right = mid - 1;
    }
    else if (nums[mid] < target) {
      left = mid + 1;
    }
    else {
      right = mid;
    }
  }
  if (nums[left] != target) {
    return([-1, -1]);
  }
  const left_border = left
  right = nums.length - 1;
  while(left <= right) {
    const mid = Math.floor(left + (right - left) / 2);
    if (nums[mid] > target) {
      right = mid - 1;
    }
    else {
      left = mid + 1;
    }
  }
  return([left_border, right])
};

ret = searchRange([5,7,7,8,8,10], 8);
console.log(ret);
