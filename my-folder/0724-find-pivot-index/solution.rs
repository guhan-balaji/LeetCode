impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let total_sum: i32 = nums.iter().sum();
        let mut sum = 0;
        for (i, val) in nums.iter().enumerate() {
            if sum == total_sum - sum - val {
                return i as i32;
            }
            sum += val;
        }
        -1
    }
}
