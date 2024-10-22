# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Method to find the k-th largest level sum of a binary tree
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        # Initialize a list to store the sum of each level
        res = []  

        # Create a queue for level-order traversal (BFS) and enqueue the root node
        q = deque([root])  

        # Traverse the tree level by level using while loop
        while q:
            # Get the number of nodes at the current level
            n = len(q)  

            # Initialize the sum of node values at the current level
            level_sum = 0  

            # Traverse nodes at the current level using for loop
            for _ in range(n):
                # Dequeue a node from the queue
                node = q.popleft()

                # Add the node value to the level sum
                level_sum += node.val

                # Enqueue the left and right child nodes (if they exist) for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Store the sum of the current level
            res.append(level_sum)  

        # If k is greater than the number of levels, return -1 (as per problem constraints)
        if k > len(res):
            return -1

        # Sort the level sums in descending order
        res.sort(reverse=True)  

        # Return the k-th largest sum (since array indices start at 0, use k-1)
        return res[k-1]