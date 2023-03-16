# zadanie domowe:
# porownaj odcinanie 1 i 2, scalanie, odcinanie 3 i scalanie z pierwszym
# z
# odcinanie 1 i 2, scalanie, odcinanie 3 i 4, scalanie, potem scalanie 1i2 z 3i4 itd


################### PONIZSZY ALGORYTM JESZCZE NIE BYL TESTOWANY I NAPRAWIANY ###################


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def merge_sorted(list1, list2):
    if list1 == None:
        return list2
    if list2 == None:
        return list1
    output_head, output_tail = None, None
    while list1 != None and list2 != None:
        if list1.val < list2.val:
            tmp = list1
            list1 = list1.next
        else:
            tmp = list2
            list2 = list2.next
        if output_tail == None:
            tail = tmp
            head = tmp
        else:
            tail.next = tmp
            tail = tail.next
        tail.next = None
    if list1 != None:
        tail.next = list1
    else:
        tail.next = list2
    return output_head


def cut_natural_series(head): # zakladamy, ze lista jest niepusta
    sorted = head
    if head.next == None:
        return head, None
    while head.next != None and head.val <= head.next.val:
        head = head.next
    unsorted = head.next
    head.next = None
    return sorted, unsorted


def merge_sort(l):
    head = l
    while True:
        l, tail = None, None
        head = None
        counter = 0
        while l != None:
            series1, l = cut_natural_series(l)
            if l == None and counter == 0:
                return series1
            counter += 1
            if l == None:
                tail.next = series1
                l = head
            break
        series2, l = cut_natural_series(l)
        merged = merge_sorted(series1, series2)
        if head is None:
            head = merged
            tail = merged
        else:
            tail.next = merged
        while tail.next != None:
            tail = tail.next
