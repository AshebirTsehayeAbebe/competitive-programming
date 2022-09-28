class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = tail = None

    def get(self, index):
        p = self.head
        for i in range(self.size):
            print(p.data)
            p=p.next
            
        if index < 0 or index >= self.size:
            return -1
        
        p = self.head
        for i in range(index):
             p = p.next
        return p.data
    def addAtHead(self, val):
        newNode = Node(val)
        if self.size==0:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head = newNode
        self.size = self.size + 1

    def addAtTail(self, val):
        newNode = Node(val)
        if self.size == 0:
            self.head = self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode
        self.size+=1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            p = self.head
            for i in range(1,index):
                 p = p.next
            node = Node(val)
            node.next=p.next
            p.next = node
            self.size+=1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if self.size == 1:
            self.head = tail = None
        elif index == 0:
            self.head = self.head.next
        else:
            p = self.head
            for i in range(1,index):
                 p = p.next
            nodeToBeDeleted = p.next
            p.next = nodeToBeDeleted.next
            if index == self.size-1:
                            self.tail = p
        self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
