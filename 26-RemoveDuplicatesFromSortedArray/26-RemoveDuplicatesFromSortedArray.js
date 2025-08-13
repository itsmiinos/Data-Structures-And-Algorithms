// Last updated: 8/13/2025, 8:24:19 PM
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 0;
    let j = 1;
    while(j<nums.length){
        if(nums[i]===nums[j]){
           j++;
        }
        else{
            i++;
            [nums[i], nums[j]] = [nums[j], nums[i]];
            j++;
        }
    }
    return i+1;
    
};