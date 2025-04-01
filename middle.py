""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    new = Node(data)
    if head is None or data < head.data:
        new.next = head
        return new
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    new.next = current.next
    current.next = new
    return head
        
        
        
