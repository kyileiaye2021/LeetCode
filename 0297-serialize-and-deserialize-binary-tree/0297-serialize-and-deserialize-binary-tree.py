# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # preorder traversal
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return 

            res.append(str(root.val))

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = data.split(',')
        i = [0]
        def dfs(i):
            if data[i[0]] == 'N':
                i[0] += 1
                return None

            new_node = TreeNode(int(data[i[0]]))
            i[0] += 1
            new_node.left = dfs(i)
            new_node.right = dfs(i)
            return new_node

        return dfs(i)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))