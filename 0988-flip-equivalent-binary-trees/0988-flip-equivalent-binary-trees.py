class Solution:
    def flipEquiv(self, root1, root2):
        """
        Checks if two trees are flip-equivalent.

        Two trees are flip-equivalent if they are the mirror image of each other.
        For example:

            1       1
           / \     / \
          2   4   4   2
          / \
         3   5   3   5

        The function returns True if the trees are flip-equivalent, False otherwise.
        """

        def checker(node1, node2):
            """
            Helper function to check if two subtrees are flip-equivalent.
            """
            # If both nodes are None, they are flip-equivalent
            if not node1 and not node2:
                return True
            # If one node is None and the other is not, or their values are different, they are not flip-equivalent
            if not node1 or not node2 or node1.val != node2.val:
                return False
            # Check if the left subtree of node1 is flip-equivalent to either the left or right subtree of node2, 
            # and the right subtree of node1 is flip-equivalent to the remaining subtree of node2
            return ((checker(node1.left, node2.left) or checker(node1.left, node2.right)) and
                    # The 'or' keyword is used to check if the left subtree of node1 can be flipped to match either the left or right subtree of node2
                    (checker(node1.right, node2.right) or checker(node1.right, node2.left)))

        # Call the checker function with the roots of the two trees
        return checker(root1, root2)