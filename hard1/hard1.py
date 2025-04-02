def swap_pairs(head):
    a = Node()
    a.next = head
    prev = a
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        first.next = second.next 
        second.next = first
        prev.next = second
        prev = first
    
    return a.next
