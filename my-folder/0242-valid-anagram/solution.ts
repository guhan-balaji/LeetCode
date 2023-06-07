function isAnagram(s: string, t: string): boolean {

    if (s.length !== t.length) return false;

    let map = new Map();

    for (let c of s) {
        if (map.has(c)) {
            map.set(c, map.get(c) + 1);
        } else {
            map.set(c, 1);
        }
    }

    for (let c of t) {
        if (map.has(c) && map.get(c) > 0) {
            map.set(c, map.get(c) - 1);
        } else {
            return false;
        }
    }

    return true;
};
