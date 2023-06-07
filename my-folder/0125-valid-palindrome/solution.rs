impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s = s.to_ascii_lowercase()
                 .chars()
                 .filter(|&c| c.is_ascii_alphanumeric())
                 .collect::<Vec<char>>();

        check(0, s.len() - 1, s)
    }


}
    fn check(i: usize, j: usize, s: Vec<char>) -> bool {
        if s.len() <= 1 || i >= s.len() / 2 {
            return true;
        }

        (s[i] == s[j]) && check(i + 1, j - 1, s)
    }
