class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        """
        This function calculates the list of boolean values indicating whether each substring of the given string s
        is a palindrome. The substrings are defined by a tree structure where each node is a character in the string
        and the edges represent the parent-child relationships.

        :type parent: List[int]
        :type s: str
        :rtype: List[bool]
        """

        # Store the length of the string
        n = len(s)

        # Create a tree structure using a dictionary
        tree = defaultdict(list)

        # Initialize the result list with False values
        self.res = [False for _ in s]

        # Create the tree structure
        for i, it in enumerate(parent):
            tree[it].append(i)

        # Define constants for the modulo operation and the base values for the hash calculations
        MOD = int(1e9+7)
        h = 26
        hh = 31

        # Initialize the last index
        lastIdx = 0

        # Initialize the list to store the sizes of the subtrees
        sizes = [0 for _ in s]

        # Define a recursive function to calculate the sizes of the subtrees
        def dfs(root):
            # Initialize the size of the current subtree to 1
            sz = 1

            # Iterate over the children of the current node
            for child in tree[root]:
                # Recursively calculate the size of the subtree rooted at the child
                sz += dfs(child)

            # Store the size of the current subtree
            sizes[root] = sz

            # Return the size of the current subtree
            return sz

        # Calculate the sizes of the subtrees
        dfs(0)

        # Create a list to store the leaves
        ls = []

        # Define a recursive function to perform the postorder traversal and calculate the hash values
        def postorder(root):
            # Initialize the size of the current subtree to the previously calculated value
            sz = sizes[root]

            # Initialize the variables for the hash calculations
            left = 0
            ss, revSS = 0, 0
            ss2, revSS2 = 0, 0

            # Iterate over the children of the current node
            for child in tree[root]:
                # Recursively calculate the hash values for the subtree rooted at the child
                res = postorder(child)

                # Calculate the hash values for the current subtree
                ss = (ss + pow(h, left, MOD) * res[0]) % MOD
                revSS = (pow(h, sizes[child], MOD) * revSS + res[1]) % MOD

                ss2 = (ss2 + pow(h, left, MOD) * res[2]) % MOD
                revSS2 = (pow(h, sizes[child], MOD) * revSS2 + res[3]) % MOD

                # Update the variable for the number of nodes in the subtree
                left += sizes[child]

            # Calculate the hash values for the current node
            ss = (ss + pow(h, left, MOD) * (ord(s[root]))) % MOD
            revSS = (revSS * pow(h, 1, MOD) + (ord(s[root]))) % MOD

            ss2 = (ss2 + pow(h, left, MOD) * (ord(s[root]))) % MOD
            revSS2 = (revSS2 * pow(h, 1, MOD) + (ord(s[root]))) % MOD

            # Store the current node in the list of leaves
            ls.append(s[root])

            # Check if the current subtree is a palindrome
            if ss == revSS and ss2 == revSS2:
                # Store the result in the result list
                self.res[root] = True

            # Return the hash values for the current subtree
            return (ss, revSS, ss2, revSS2)

        # Perform the postorder traversal
        postorder(0)

        # Return the result list
        return self.res