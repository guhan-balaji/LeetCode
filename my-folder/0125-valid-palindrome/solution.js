/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

    return check(0, s.length - 1, s);
};

function check(i, j, s) {
    if (s.length <= 1 || i >= s.length / 2) {
        return true;
    }

    return (s[i] === s[j]) && check(i + 1, j - 1, s);
}
