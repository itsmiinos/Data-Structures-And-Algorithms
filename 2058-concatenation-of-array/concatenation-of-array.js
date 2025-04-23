/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let ans = new Array(nums.length*2);
    let k = 0;
    for(let i=0;i<nums.length;i++){
        ans[k] = nums[i];
        k++;
    }
    for(let i=0;i<nums.length;i++){
        ans[k] = nums[i];
        k++;
    }
    return ans;
};