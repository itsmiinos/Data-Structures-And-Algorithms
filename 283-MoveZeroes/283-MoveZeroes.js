// Last updated: 8/13/2025, 8:20:28 PM
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let i = 0;
    for(let j = 0;j<nums.length;j++){
        if(nums[j]!==0){
            [nums[i] , nums[j]] = [nums[j] , nums[i]];
            i++;
        }
    }
};