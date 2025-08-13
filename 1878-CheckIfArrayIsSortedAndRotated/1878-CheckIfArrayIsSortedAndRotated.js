// Last updated: 8/13/2025, 8:16:59 PM
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var check = function(nums) {
    let count = 0;
    for(let i = 1; i<nums.length; i++){
        if(nums[i-1] > nums[i]){
            count++;
        }
        if(i=== nums.length-1 ){
            if(nums[i] > nums[0]){
                count++;
            }
        }
    }
    if(count<=1){
        return true;
    }
    return false;
};