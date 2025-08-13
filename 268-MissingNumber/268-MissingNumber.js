// Last updated: 8/13/2025, 8:20:30 PM
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let res = nums.length;
    for(let i=0;i<nums.length;i++){
        res += i - nums[i];
    }
    return res;
};