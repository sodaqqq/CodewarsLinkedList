def linked_list_from_string(s):
    head = None
    current = None
    s = s.strip().split(' -> ')
    for i in s[:-1]:
        node = Node(int(i))
        if head is None:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head
        
        
