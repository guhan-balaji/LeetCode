/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// var twoSum = function(nums, target) {
    
// };

function twoSum(nums, target) {
    const numToIndex = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (numToIndex.has(target - nums[i])) {
            return [numToIndex.get(target - nums[i]), i]
        }
        numToIndex.set(nums[i], i)
    }
    return []
}
