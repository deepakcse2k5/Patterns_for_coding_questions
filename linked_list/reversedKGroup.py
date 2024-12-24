class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def reversedKGroup(head, k):
    def reverseLinkedList(start, end):
        prev , curr = None, start
        while curr!=end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy

    while True:
        kth = prev_group
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
    
        group_start = prev_group.next
        group_end = kth.next

        reverseLinkedList(group_start, group_end)

        prev_group.next = kth
        group_start.next = group_end

        prev_group = group_start

def print_list(head):
    while head:
        print(head.val, end="-->")
        head = head.next
    print("None")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
k = 3
new_head = reversedKGroup(head, k)
print_list(new_head)
                 


            
