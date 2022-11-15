impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let mut s = s.chars().peekable();
        for c in t.chars() {
            match s.peek() {
                Some(&ch) if ch == c => {
                    s.next();
                },
                _ => {},
            }
        }
        s.next().is_none()
    }
}
