class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  # for first value head will be None
        print(self.head)
        self.head = node  # for next upcoming value we will update the head value to node for adding to beginning
        # since we are adding node in the same linked list so the head value will keep on updating

    def print_element_in_linked_list(self):
        if self.head is None:
            print('Linked List is empty')
        node = self.head

        ll_print = ''
        while node:
            ll_print += str(node.data) + '--->'
            node = node.next
        print(ll_print)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.print_element_in_linked_list()