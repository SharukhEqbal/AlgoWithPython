class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        print(self.head)
        self.head = node

    def print_element_in_linked_list(self):
        if self.head is None:
            print('Linked List is empty')
        node = self.head

        ll_print = ''
        while node:
            ll_print += str(node.data) + '--->'
            node = node.next
        print(ll_print)

    # O(N) time complexity and O(1) complexity
    # step1: start from the head step2: check ll is empty or not if not then iterate through ll till node.data = value
    # it will come out of while loop if value is not found(in that node value becomes None(tail) or value is found)
    def search_a_value_in_ll(self, value):
        # self.head is itself a node the starting node contains both data and next value
        node = self.head
        print(self.head)
        while node is not None and node.data != value:
            node = node.next
        return node is not None


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.print_element_in_linked_list()
    print(ll.search_a_value_in_ll(5))