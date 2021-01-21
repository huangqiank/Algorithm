class Treenode:
    def __init__(self,x):
        self.value=x
        self.left = None
        self.right = None

def find_path(node,k):
    sum = 0
    path=[]
    return find_path_help(node,k,path,sum)

def find_path_help(node,k,path,sum):
    if node is None:
        return False
    sum+=node.value
    if  sum == k and node.left is None and  node.right is None:
        return True,path
    else:
        return find_path_help(node.left,k,path + [node.value],sum) or find_path_help(node.right,k,path+[node.value],sum)

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)
root.right.left = Treenode(6)
root.right.right = Treenode(7)
print find_path(root,10)
node1 = Treenode(1)
node2 = Treenode(2)
node3 = Treenode(3)
node4 = Treenode(4)
node5 = Treenode(5)
node6 = Treenode(6)
node1.left = node2
node1.right = node3
node2.left= node4
node4.left = node6
node3.left = node5
print find_path(node1,4)
a=[1,2,3,4,"#","#",1]
print a.index('#')

if "#" in a:
    for i in range(a.index('#'),len(a),1):
            if a[i]!='#':
                print False
                break
print True