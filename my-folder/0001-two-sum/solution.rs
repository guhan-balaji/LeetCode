impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        let mut num_to_index: HashMap<i32, i32> = HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if num_to_index.contains_key(&complement) {
                if let Some(&idx) = num_to_index.get(&complement) {
                    return vec![idx, i as i32];
                }
            }
            num_to_index.insert(num, i as i32);
        }
        vec![]
    }
}
