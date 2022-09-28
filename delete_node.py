class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
class Solution:
    def deleteNode(self, node):
        prev = Node()
        if(node == None):
            return
        else:
            while(node.next != None):
                node.val = node.next.val
                prev = node
                node = node.next
            prev.next = None        
