impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut v = nums.clone();
        for i in 1..v.len() {
            v[i] += v[i - 1];
        }    
        v
    }
}
