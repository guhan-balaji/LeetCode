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

function middleNode(head: ListNode | null): ListNode | null {
    const length = noOfNodes(head, 0);
    const mid = Math.floor(length / 2) + 1;

    return (length === 0)? null : findNode(head, 1, mid); 
};

function findNode(head: ListNode, idx: number, target: number): ListNode {
    if (idx === target) return head;

    return findNode(head.next, idx + 1, target);
}

function noOfNodes(head: ListNode | null, size: number): number {
    if (head === null) {
        return size;
    } else {
        return noOfNodes(head.next, size + 1)
    }
}
