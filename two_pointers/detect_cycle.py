from linked_list import LinkedList

def detect_cycle(head):
    slow , fast = head, head

    while fast  and fast.next :
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False


print(detect_cycle( [2, 4, 6, 8, 10, 12]))