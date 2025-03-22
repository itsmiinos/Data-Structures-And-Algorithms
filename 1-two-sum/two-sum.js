/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let sumMap = new Map();
    for(let i=0;i<nums.length;i++){
        const diff = target - nums[i];
        if(sumMap.has(diff)){
            return [i,sumMap.get(diff)];
        }
        else{
            sumMap.set(nums[i],i);
        }
    }
};