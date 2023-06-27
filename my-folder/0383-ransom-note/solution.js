/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const map = new Map();

    for (c of magazine) {
        if (map.has(c)) {
            map.set(c, map.get(c) + 1);
        } else {
            map.set(c, 1);
        }
    }

    for (c of ransomNote) {
        if (!map.has(c)) return false;

        if (map.get(c) < 1) return false;

        map.set(c, map.get(c) - 1);
    }

    return true;
};
