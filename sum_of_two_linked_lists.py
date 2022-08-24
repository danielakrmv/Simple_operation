class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        elems = []
        current = self.head
        while current != None:
            elems.append(current.data)
            current = current.next
        return elems

    def append(self, data):
        elem = Node(data)
        if self.head == None:
            self.head = elem
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = elem


def addTwoLists(first_list, second_list):
    third_list = LinkedList()
    carry = 0

    first_node = first_list.head
    second_node = second_list.head
    while first_node or second_node or carry:
        if first_node:
            carry += first_node.data
            first_node = first_node.next
        if second_node:
            carry += second_node.data
            second_node = second_node.next

        third_list.append(carry % 10)
        carry = carry // 10

    return third_list


list1 = LinkedList()
list2 = LinkedList()
list1.append(7)
list1.append(1)
list1.append(6)
print(list1.display())
list2.append(5)
list2.append(9)
list2.append(2)
print(list2.display())
ll = addTwoLists(list1, list2)
print(ll.display())
