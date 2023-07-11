function maxSubArray(nums: number[]): number {
    let maxSum = nums[0];

    let sum = nums[0];

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > sum && nums[i] + sum < nums[i]) {
            sum = nums[i];
        } else {
            sum += nums[i]
        }

        if (sum > maxSum) {
            maxSum = sum;
        }
    }

    return maxSum;
};
