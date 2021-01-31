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
    def search_a_value_in_ll(self, value):
        # self.head is itself a node the starting node contains both data and next value
        node = self.head
        print(self.head)
        while node is not None and node.data != value:
            node = node.next
        return node is not None

    def get_length(self):
        print('hello')
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count += 1
        return count

    # step1: check whether the node is head or tail, if head or tail then handle that case by updating the s.node
    # step2: before removing the node take a tempNode or update the surrounding node before removing the node
    # step3: once the surrounding node is updated then go for removal of the node
    def remove_a_node_at_an_index(self, index):
        if index < 0 or index >= self.get_length():
            print('invalid index')
            return

        node = self.head
        count = 0
        if index == count:
            self.head = None
        while node:
            if count == index-1:
                node.next = node.next.next
                break
            count += 1
            node = node.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(119)
    ll.print_element_in_linked_list()
    #print(ll.search_a_value_in_ll(5))
    #print(ll.get_length())
    print(ll.remove_a_node_at_an_index(1))
    ll.print_element_in_linked_list()
