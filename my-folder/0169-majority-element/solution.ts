function majorityElement(nums: number[]): number {

    if (nums.length === 1) return nums[0];

    const map = new Map();
    for (let i of nums) {
        if (map.has(i)) {
            if (map.get(i) + 1 > Math.floor(nums.length / 2)) return i;
            map.set(i, map.get(i) + 1);
        } else {
            map.set(i, 1);
        }
    }
};
