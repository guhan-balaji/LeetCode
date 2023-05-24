/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    for (let c of s) {
        if (c === '(' || c === '{' || c === '[') {
            stack.push(c);
        } else {
            const top = stack.pop()
            if (top === '(' && c === ')' || 
                top === '{' && c === '}' || 
                top === '[' && c === ']') {
            } else {
                return false;
            }
        }
    }
    return stack.length === 0;
};
