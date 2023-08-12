class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class Tree:
    def createnode(self,data):
        return Node(data)

    def insertion(self,node,data):
        if node is None:
            return self.createnode(data)

        if node.data > data:
            node.left=self.insertion(node.left,data)
        else:
            node.right=self.insertion(node.right,data)
        return node



    def display(self,node):

        if node is not None:
            self.display(node.left)
            print(node.data)
            self.display(node.right)

    def deletion(self,node,data):

        if node.data > data:
            node.left=self.deletion(node.left,data)

        elif node.data < data:
            node.right=self.deletion(node.right,data)

        else:
            if node.left==None and node.right==None:
                return None

            elif node.left==None:
                return node.right

            elif node.right == None:
                 return node.left

            node.data=self.deletehelper(node.right)
            node.right=self.deletion(node.right,node.data)

        return node


    def deletehelper(self,node):
        while node.left:
            node=node.left
        return node.data
    # def roottoleaf(self,node,arr=[]):
    #     arr.append([node.data])
    #
    #     if node.left:
    #         self.roottoleaf(node.left)
    #     elif node.right:
    #         self.roottoleaf(node.right)
    #     else:
    #         print("_________________________________")
    #         print(arr)
    #         arr.pop()
    #         return
    def roottoleaf(self, node, arr=None):
        if arr is None:
            arr = []
        arr.append(node.data)

        if node.left:
            self.roottoleaf(node.left, arr)
        if node.right:
            self.roottoleaf(node.right, arr)
        if not node.left and not node.right:
            string = '---->'.join(map(str, arr))
            print(string)


        arr.pop()


tree=Tree()
root=tree.createnode(10)
tree.insertion(root,5)
tree.insertion(root,4)
tree.insertion(root,3)
tree.insertion(root,1)
tree.insertion(root,12)
tree.insertion(root,11)
tree.insertion(root,8)
tree.insertion(root,20)
tree.display(root)

print()
print()
tree.display(root)
tree.roottoleaf(root)

