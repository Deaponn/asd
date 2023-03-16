class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head): # print linked list
    array = []
    curr = head
    while curr is not None:
        array.append(curr.val)
        curr = curr.next
    print(array)


def add(head, number): # add a number at the beginning
    newHead = Node(number)
    newHead.next = head
    return newHead


def insert(head: Node, number): # insert to a sorted list
    newNode = Node(number)
    if head == None:
        return newNode
    if head.val >= number:
        newNode.next = head
        return newNode
    if head.next is None:
        head.next = newNode
        return head
    current: Node = head
    while current.next is not None:
        if current.next.val >= number:
            newNode.next = current.next
            current.next = newNode
            return head
        current = current.next
    current.next = newNode
    return head


def remove_maximum(head: Node): # remove maximum link from unsorted list, return the removed link
    pointer = Node(None)
    pointer.next = head
    max_val = head.val
    max_pointer = head
    while pointer.next is not None:
        if pointer.next.val > max_val:
            max_val = pointer.next.val
            max_pointer = pointer
        pointer = pointer.next
    output = max_pointer.next
    if max_pointer.next is not None:
        max_pointer.next = max_pointer.next.next
    return head, output


def insertion_sort(head: Node): # insertion sort using above methods
    pointer = head
    output = None
    while pointer is not None:
        output = insert(output, pointer.val)
        pointer = pointer.next
    return output


def selection_sort(head: Node): # selection sort using above methods
    head, removed = remove_maximum(head)
    output = Node(removed.val)
    while head.next is not None:
        head, removed = remove_maximum(head)
        output = add(output, removed.val)
    output = add(output, head.val)
    return output


# testing insert
# head = insert(None, 3)
# head = insert(head, 2)
# head = insert(head, 6)
# head = insert(head, 4)
# head = insert(head, 7)
# head = insert(head, 5)
# head = insert(head, 1)
# head = insert(head, 8)

# print_list(head)

# head = insert(None, 1)
# head = insert(head, 2)
# head = insert(head, 3)
# head = insert(head, 6)
# head = insert(head, 7)
# head = insert(head, 4)
# head = insert(head, 6)
# head = insert(head, 5)
# head = insert(head, 2)
# head = insert(head, 6)
# head = insert(head, 7)

# print_list(head)


# testing remove_maximum
# head = add(None, 6)
# head = add(head, 2)
# head = add(head, 5)
# head = add(head, 6)
# head = add(head, 4)
# head = add(head, 6)
# head = add(head, 3)
# head = add(head, 7)
# head = add(head, 1)

# head, rem1 = remove_maximum(head)
# head, rem2 = remove_maximum(head)
# head, rem3 = remove_maximum(head)

# print_list(head)
# print(rem1.val, rem2.val, rem3.val)


# testing insertion sort
# head = add(None, 6)
# head = add(head, 2)
# head = add(head, 5)
# head = add(head, 6)
# head = add(head, 4)
# head = add(head, 6)
# head = add(head, 3)
# head = add(head, 7)
# head = add(head, 1)

# head = insertion_sort(head)

# print_list(head)


# testing selection sort
# head = add(None, 6)
# head = add(head, 2)
# head = add(head, 5)
# head = add(head, 6)
# head = add(head, 4)
# head = add(head, 6)
# head = add(head, 3)
# head = add(head, 7)
# head = add(head, 1)

# head = selection_sort(head)

# print_list(head)