/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function(isBadVersion: any) {

    return function(n: number): number {
        return rec(1, n);
    };

    function rec(min: number, max: number): number {
        if (min === max) return min;
        if (min + 1 === max) {
            return isBadVersion(min)? min : max;
        } 

        const mid = min + Math.floor((max - min) / 2);

        return isBadVersion(mid)? rec(min, mid) : rec(mid + 1, max) 
    }
};
