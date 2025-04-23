/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let mySet = new Set();
    for(let i = 0; i<nums.length ; i++){
        if(!mySet.has(nums[i])){
            mySet.add(nums[i]);
        }
        else{
            return true;
        }
    }
    return false;
};