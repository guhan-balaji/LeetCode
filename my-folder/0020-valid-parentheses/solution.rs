impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = vec![];
        for c in s.chars() {
            if c == '(' || c == '{' || c == '[' {
                stack.push(c);
            } else {
                if let Some(top) = stack.pop() {
                    if top == '(' && c == ')'||
                       top == '{' && c == '}'||
                       top == '[' && c == ']' {                       
                       } else {
                           return false;
                       }
            } else {
                return false;
            }
            }
        }
        stack.len() == 0
    }
}
