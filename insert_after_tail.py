import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def printLinkedList(head):
    cur_node = head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next


def insertNodeAtTail(head, data):
    item = SinglyLinkedListNode(data)

    if head is None:
        head = item
    else:
        n = head

        while (n.next):
            n = n.next

        n.next = item

    return head


if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    printLinkedList(llist.head)