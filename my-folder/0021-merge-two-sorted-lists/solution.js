/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    if (list1 === null && list2 === null) {
        return null;
    } else if (list1 === null) {
        return list2;
    } else if (list2 === null) {
        return list1;
    }
    let head = null;
    if (list1.val < list2.val) {
        head = list1;
        head.next = mergeTwoLists(list1.next, list2);
    } else {
        head = list2;
        head.next = mergeTwoLists(list1, list2.next);
    }

    return head;
};
