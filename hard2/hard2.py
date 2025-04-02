class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise Exception()
    
    current = head.next.next
    first_head = head
    second_head = head.next
    current_first = first_head
    current_second = second_head
    
    while current:
        current_first.next = current
        current_first = current_first.next
        current = current.next
        
        if current:
            current_second.next = current
            current_second = current_second.next
            current = current.next
    
    current_first.next = None
    current_second.next = None
    
    return Context(first_head, second_head)
