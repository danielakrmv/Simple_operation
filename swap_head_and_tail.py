class MyNode:
    def __init__(self, data, next = None):
         self.data = data
         self.next = next


class MyList:
    def __init__(self):
         self.head = None
         self.tail = None

    def push_back(self, data):
        if self.tail is None:
            self.head = MyNode(data)
            self.tail = self.head
        else:
            self.tail.next = MyNode(data)
            self.tail = self.tail.next

    def dump(self):
        node = self.head
        while node is not None:
            print(node.data, end=' -> ')
            node = node.next
        print('end of the linked list')

    def swap(self):
        # For empty and size 1, no change.

        if self.head is None: return
        if self.head.next is None: return

        # For size 2, easy swap. if we have only A and B for example

        if self.head.next.next is None:
            self.tail.next = self.head
            self.head.next = None
            self.head, self.tail = self.tail, self.head
            return

        # For size 3+, little more complex, need the
        # penultimate node as well as head and tail.

        current = self.head
        while current.next != self.tail:
            current = current.next

        self.tail.next = self.head.next
        self.head.next = None
        current.next = self.head
        self.head, self.tail = self.tail, self.head


llist = MyList()
llist.push_back('A')
llist.push_back('B')
llist.push_back('C')
llist.push_back('D')

llist.dump()

llist.swap()

llist.dump()