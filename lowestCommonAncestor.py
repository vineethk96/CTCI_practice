class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    # Enter your code here
    stackV1 = []
    stackV2 = []

    # print("v1----")
    nodeV1, stackV1 = preOrder(root, v1, stackV1)
    # print("v2----")
    nodeV2, stackV2 = preOrder(root, v2, stackV2)

    return commonStack(stackV1, stackV2)


# Use a Depth-First Search to find each node
def preOrder(node, var, stack):
    if node != None:
        stack.append(node)
        # print("Node: " + str(node.info))

        if node.info > var:  # var is less than node
            varNode, stack = preOrder(node.left, var, stack)
        elif node.info < var:  # var is greater than node
            varNode, stack = preOrder(node.right, var, stack)

    return node, stack


def commonStack(stackV1, stackV2):
    hashMap = {}

    for node in stackV1:
        hashMap.update({node.info: node})
        # print(hashMap[node.info])

    while stackV2:
        node = stackV2.pop()

        if node.info in hashMap:
            return hashMap[node.info]


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
