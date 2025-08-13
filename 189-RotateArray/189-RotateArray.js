// Last updated: 8/13/2025, 8:21:33 PM
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k = k%nums.length;
    rotateSubArray(0,nums.length-1,nums);
    rotateSubArray(0,k-1,nums);
    rotateSubArray(k,nums.length-1,nums);
};

const rotateSubArray = (i,j,arr) => {
    while(i<j){
        [arr[i],arr[j]] = [arr[j],arr[i]];
        i++;
        j--;
    }
}