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

function diameterOfBinaryTree(root: TreeNode | null): number {
    return diameter(root, 0);
};

function diameter(root: TreeNode | null, dm: number): number {
    if (root === null) return dm;

    const ld = diameter(root.left, dm);
    const rd = diameter(root.right, dm);

    const maxDm = Math.max(ld, rd);

    return Math.max(maxDm, maxDepth(root.left, 1) + maxDepth(root.right, 1) - 2);
}

function maxDepth(root: TreeNode | null, depth: number): number {
    if (root === null) return depth;

    const ld = maxDepth(root.left, depth + 1);
    const rd = maxDepth(root.right, depth + 1);

    return ld > rd? ld: rd;
}
