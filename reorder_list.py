class Solution(object):
    def reorderList(self, head):
        list = []
        while head:
            list.append(head)
            head = head.next
        p = backup = ListNode(0)

        while len(list)>1:
            first = list.pop(0)
            second = list.pop()
            p.next = first
            first.next = second
            p = second
            p.next = None
        
        if list: 
            p.next = list.pop()
            p = p.next
            p.next = None
        return backup.next
