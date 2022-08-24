class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next

  def append(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return

    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def prepend(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node

  def insert_after_node(self, prev_node, data):

    if not prev_node:
      print("Previous node does not exist.")
      return

    new_node = Node(data)

    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key):

    cur_node = self.head

    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      cur_node = None
      return

    prev = None
    while cur_node and cur_node.data != key:
      prev = cur_node
      cur_node = cur_node.next

    if cur_node is None:
      return

    prev.next = cur_node.next
    cur_node = None


  def delete_node_at_pos(self, pos):
    if self.head:
      cur_node = self.head
      if pos == 0:
        self.head = cur_node.next
        cur_node = None
        return

      prev = None
      count = 0
      while cur_node and count != pos:
          prev = cur_node
          cur_node = cur_node.next
          count += 1

      if cur_node is None:
          return

      prev.next = cur_node.next
      cur_node = None

  def len_iterative(self):
    count = 0
    cur_node = self.head
    while cur_node:
      count += 1
      cur_node = cur_node.next
    return count

  def len_recursive(self, node):
    if node is None:
      return 0
    return 1 + self.len_recursive(node.next)

  def swap_nodes(self, key_1, key_2):

    if key_1 == key_2:
      return

    prev_1 = None
    curr_1 = self.head
    while curr_1 and curr_1.data != key_1:
      prev_1 = curr_1
      curr_1 = curr_1.next

    prev_2 = None
    curr_2 = self.head
    while curr_2 and curr_2.data != key_2:
      prev_2 = curr_2
      curr_2 = curr_2.next

    if not curr_1 or not curr_2:
      return

    if prev_1:
      prev_1.next = curr_2
    else:
      self.head = curr_2

    if prev_2:
      prev_2.next = curr_1
    else:
      self.head = curr_1

    curr_1.next, curr_2.next = curr_2.next, curr_1.next

  def print_helper(self, node, name):
    if node is None:
      print(name + ": None")
    else:
      print(name + ":" + node.data)

  def reverse_iterative(self):

    prev = None
    cur = self.head
    while cur:
      nxt = cur.next
      cur.next = prev

      self.print_helper(prev, "PREV")
      self.print_helper(cur, "CUR")
      self.print_helper(nxt, "NXT")
      print("\n")

      prev = cur
      cur = nxt
    self.head = prev

  def reverse_recursive(self):

    def _reverse_recursive(cur, prev):
      if not cur:
        return prev

      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
      return _reverse_recursive(cur, prev)

    self.head = _reverse_recursive(cur=self.head, prev=None)

  def merge_sorted(self, llist):

    p = self.head
    q = llist.head
    s = None

    if not p:
        return q
    if not q:
        return p

    if p and q:
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s
    while p and q:
        if p.data <= q.data:
            s.next = p
            s = p
            p = s.next
        else:
            s.next = q
            s = q
            q = s.next
    if not p:
        s.next = q
    if not q:
        s.next = p

    self.head = new_head
    return self.head

  def remove_duplicates(self):
    cur = self.head
    prev = None
    dup_values = dict()

    while cur:
      if cur.data in dup_values:
        # Remove node:
        prev.next = cur.next
        cur = None
      else:
        # Have not encountered element before.
        dup_values[cur.data] = 1
        prev = cur
      cur = prev.next

  def print_nth_from_last(self, n, method):
    if method == 1:
      # Method 1:
      total_len = self.len_iterative()
      cur = self.head
      while cur:
        if total_len == n:
          # print(cur.data)
          return cur.data
        total_len -= 1
        cur = cur.next
      if cur is None:
        return

    elif method == 2:
      # Method 2:
      p = self.head
      q = self.head

      if n > 0:
        count = 0
        while q:
          count += 1
          if (count >= n):
            break
          q = q.next

        if not q:
          print(str(n) + " is greater than the number of nodes in list.")
          return

        while p and q.next:
          p = p.next
          q = q.next
        return p.data
      else:
        return None

  def count_occurences_iterative(self, data):
    count = 0
    cur = self.head
    while cur:
      if cur.data == data:
        count += 1
      cur = cur.next
    return count

  def count_occurences_recursive(self, node, data):
    if not node:
      return 0
    if node.data == data:
      return 1 + self.count_occurences_recursive(node.next, data)
    else:
      return self.count_occurences_recursive(node.next, data)

  def rotate(self, k):
    if self.head and self.head.next:
      p = self.head
      q = self.head
      prev = None
      count = 0

      while p and count < k:
        prev = p
        p = p.next
        q = q.next
        count += 1
      p = prev
      while q:
        prev = q
        q = q.next
      q = prev

      q.next = self.head
      self.head = p.next
      p.next = None

    def is_palindrome_1(self):
      # Solution 1:
      s = ""
      p = self.head
      while p:
        s += p.data
        p = p.next
      return s == s[::-1]

    def is_palindrome_2(self):
      # Solution 2:
      p = self.head
      s = []
      while p:
        s.append(p.data)
        p = p.next
      p = self.head
      while p:
        data = s.pop()
        if p.data != data:
          return False
        p = p.next
      return True

    def is_palindrome_3(self):
      if self.head:
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
          prev.append(q)
          q = q.next
          i += 1
        q = prev[i - 1]

        count = 1

        while count <= i // 2 + 1:
          if prev[-count].data != p.data:
            return False
          p = p.next
          count += 1
        return True
      else:
        return True

    def is_palindrome(self, method):
      if method == 1:
        return self.is_palindrome_1()
      elif method == 2:
        return self.is_palindrome_2()
      elif method == 3:
        return self.is_palindrome_3()


llist = LinkedList()
llist.append("B")
llist.append("C")

llist.prepend("A")
llist.insert_after_node(llist.head.next.next, "D")
llist.print_list()
print("The length of the linked list calculated recursively after inserting 4 elements is:")
print(llist.len_recursive(llist.head))
print("The length of the linked list calculated iteratively after inserting 4 elements is:")
print(llist.len_iterative())

print(llist.print_nth_from_last(4,1))
print(llist.print_nth_from_last(4,2))

llist.delete_node("B")
llist.delete_node("E")
llist.delete_node_at_pos(0)

llist.print_list()

llist.swap_nodes("C", "D")
llist.print_list()

llist.reverse_iterative()

llist.print_list()

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist_2 = LinkedList()
llist_2.append(1)
llist_2.append(2)
llist_2.append(1)
llist_2.append(3)
llist_2.append(1)
llist_2.append(4)
llist_2.append(1)
print(llist_2.count_occurences_iterative(1))
print(llist_2.count_occurences_recursive(llist_2.head, 1))

'''
We create a class called Node. In the constructor of this class, 
we give the argument of self and data on line 2. 
Every node is going to consist of data and next. 
We define self.data equal to data that is passed into the constructor of the object of class Node (line 3). 
We set self.next equal to None on line 4. 
This is something that we’ll set again as we make use of the node, 
but for now, we just set it to None. That’s pretty much all we need for the Node class right now.

On line 6, we define a LinkedList class, and in the constructor, we again pass self. 
On line 8, we define the head pointer, which will point to the first node in the linked list. 
Initially, we just set it equal to None.

We define a new_node using our Node class on line 11. It consists of the data and the next field. 
We pass in data to the append method, and 
the data field in new_node has the entry of data that we passed to the append method.
we check if the linked list is empty by checking the head of the linked list. 
If the self.head is None on line 12, it implies that it’s an empty linked list and there’s nothing there. 
The head pointer doesn’t point to anything at all, and therefore there is no node in the linked list. 
If there is no node in the linked list, we set the head pointer to the new_node that we created on line 13. 
In the next line, we simply return. 
The case of an empty linked list is relatively easy to handle.

If the linked list is not empty. We have new_node that we create, and we want to append it to the linked list. 
We can start from the head pointer and then move through each of the nodes in the linked list until we get to the end, 
i.e. None. 
Once we arrive at the location that we want to insert the new_node

On line 15, we define last_node which is initially equal to the head. This implies we’re at the start of the linked list. 
We have named the variable we defined on line 15 last_node because that’s what it will eventually point to. 
It will start at the beginning of the linked list and move through the linked list 
as long as the last_node.next doesn’t point to None. 
We keep moving from node to node on line 17 until we get to the last_node where last_node.next will point to None 
and will terminate the while loop on line 16. After the while loop concludes, last_node points to the last node. 
On line 18, we input our new_node into the linked list by setting the next of last_node to new_node 
which has its own next pointing to None.

print_list is a class method, so it will take self as an argument and print out the entries of a linked list. We will start from the head pointer and print out the data component of the node and then move to the next node. We’ll keep a check on the next node to make sure it is not None. If it’s not, we move to the next node. This way, we keep printing out data until we’ve hit the null terminating component of the linked list.
We initialize cur_node equal to the head of the linked list. Then we use a while loop which keeps running and printing the data if cur_node is not equal to None.
We append four elements to the linked list.

we create a new method called insert_after_node on line 32. It takes self since it is a class method. It also takes prev_node which is the previous node after which we have to insert the new node and data which we’ll use to make the new_node.

As mentioned before, we first want to check if the prev_node is None or not. If prev_node is None or does not exist, 
then we print the following on line 34:Previous node does not exist.
and return on line 35.

If prev_node is not None, then we create a new node on line 36. 
on line 38, we point the next of the new_node to the next node of the node after which the insertion has to take place.
we set the prev_node.next to the new_node on line 39 so that the new_node now comes after the prev_node.


'''
llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)


def sum_two_lists(self, llist):
  pass