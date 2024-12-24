from linked_list_node import LinkedListNode
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    def create_linked_list(self, lst):
        for i in reversed(lst):
            new_node = LinkedListNode(i)
            self.insert_at_head(new_node)

    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
            result +=""
        return result