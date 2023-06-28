/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isBalanced(root: TreeNode | null): boolean {
    if (root === null) return true;

    const ld = maxDepth(root.left, 1);
    const rd = maxDepth(root.right, 1);

    return Math.abs(ld - rd) > 1? false: isBalanced(root.left) && isBalanced(root.right);
};

function maxDepth(root: TreeNode | null, depth: number): number {
    if (root === null) return depth;

    const ld = maxDepth(root.left, depth + 1);
    const rd = maxDepth(root.right, depth + 1);

    return (ld > rd)? ld: rd;
}
