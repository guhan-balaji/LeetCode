/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function hasCycle(head: ListNode | null): boolean {
    return traverse(head, head?.next);
};

function traverse(s: ListNode | null, f: ListNode | null): boolean {
    if (s === null || f === null) return false;

    if (s === f) return true;

    return false || traverse(s.next, f?.next?.next);
}
