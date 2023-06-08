function search(nums: number[], target: number): number {
    if (nums.length < 1) return -1;

    return bs(0, nums.length - 1, nums, target);
};

function bs(i: number, j: number, nums: number[], target: number): number {
    if (i > j || nums[i] === undefined || nums[j] === undefined) return -1;
    if (i === j) {
        return (target === nums[i])? i : -1; 
    }

    const mid = Math.floor((i + j) / 2);

    if (target === nums[mid]) return mid;

    if (target > nums[mid]) {
        return bs(mid + 1, j, nums, target);
    } else {
        return bs(i, mid - 1, nums, target);
    }
    
}
