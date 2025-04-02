def remove_duplicates(head):
    if head is None:
        return None
    
    current = head
    
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head  
