class ListNode:

    def __init__(self, value):
        self.head = None
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head: ListNode | None = None

    def insert_node(self, node: ListNode):

        if self.head is None:
            self.head = node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next
            temp.next = node

    def traverse_linked_list(self):
        temp = self.head

        while temp:
            print(temp.value, end=' ')
            temp = temp.next


l = LinkedList()

l.insert_node(ListNode(20))
l.insert_node(ListNode(30))
l.insert_node(ListNode(40))
l.insert_node(ListNode(50))
l.insert_node(ListNode(60))
l.traverse_linked_list()
l.insert_node(ListNode(80))
