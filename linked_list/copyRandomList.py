class Node:
    def __init__(self, val=0, next=None, random=None) -> None:
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head :
        return None
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next
    
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    
    curr = head
    new_head = head.next
    while curr:
        new_node = curr.next
        curr.next = new_node.next
        if new_node.next:
            new_node.next = new_node.next.next
        curr = curr.next
    return new_head

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

node1 = Node(3)
node2 = Node(7)
node3 = Node(4)
node4 = Node(5)

# Creating original linked list: 3 -> 7 -> 4 -> 5
node1.next = node2
node2.next = node3
node3.next = node4

# Setting up random pointers
node1.random = None
node2.random = node4  # 7 -> 5
node3.random = node1  # 4 -> 3
node4.random = node2  # 5 -> 7

# Deep copy the linked list
new_head = copyRandomList(node1)

# Print copied list
printList(new_head)






        