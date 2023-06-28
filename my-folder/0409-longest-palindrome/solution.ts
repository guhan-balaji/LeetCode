function longestPalindrome(s: string): number {
    const map = new Map();

    for (const c of s) {
        if (map.has(c)) {
            map.set(c, map.get(c) + 1);
        } else {
            map.set(c, 1);
        }
    }

    let res = 0;
    let hasOddChars = false;
    
    for (const i of map.values()) {
        if (i % 2 === 0) {
            res += i; 
        } else {
            hasOddChars = true;
            res += i - 1;
        }
    }

    return hasOddChars? res + 1: res;
};
