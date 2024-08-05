#!/usr/bin/env python3

from singly_linked_list import Node, SinglyLinkedList

def merge_2_lists(head1, head2):
    if not head1 and not head2:
        return None
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data <= head2.data:
        head_result = head1
        iter1 = head1.next
        iter2 = head2 
    else:
        head_result = head2
        iter1 = head1
        iter2 = head2.next
    current = head_result
    while iter1 and iter2:
        if iter1.data <= iter2.data:
            current.next = iter1
            iter1 = iter1.next
        else:
            current.next = iter2
            iter2= iter2.next
        current = current.next
    while iter1:
        current.next = iter1
        iter1 = iter1.next
        current = current.next
    while iter2:
        current.next = iter2
        iter2 = iter2.next
        current = current.next
    return head_result

if __name__ == "__main__":
    sll1 = SinglyLinkedList()
    sll1.append(1)
    sll1.append(2)
    sll1.append(4)
    sll2 = SinglyLinkedList()
    sll2.append(1)
    sll2.append(3)
    sll2.append(4)
    result = SinglyLinkedList()
    result.head = merge_2_lists(sll1.head, sll2.head)
    result.print_list()


