#!/usr/bin/env python3

class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        list_middle = self.size // 2
        if index > list_middle:
            iter = self.size - 1 
            current_node = self.tail
            while current_node and iter >= index:
                if iter == index:
                    return current_node.data
                iter -= 1
                current_node = current_node.prev
        if index <= list_middle:
            iter = 0
            current_node = self.head
            while current_node and iter <= index:
                if iter == index:
                    return current_node.data
                iter += 1
                current_node = current_node.next
        return None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_at_index(self, index, data):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return
        current_node = self.head
        iter = 0
        while current_node and iter <= index:
            if iter == index:
                new_node = Node(data)
                previous_node = current_node.prev
                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current_node
                current_node.prev = new_node
                return
            iter += 1
            current_node = current_node.next
        self.size += 1

    def delete(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                if current_node == self.tail:
                    self.tail = current_node.prev
                self.size -= 1
                return
            current_node = current_node.next

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return None
        current_node = self.head
        iter = 0
        while current_node and iter <= index:
            if iter == index:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                if current_node == self.tail:
                    self.tail = current_node.prev
                self.size -= 1
                return
            iter += 1
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.prepend(1)
    dll.append(3)
    dll.add_at_index(1,2)
    dll.print_list()
    print(dll.get(1))
    dll.delete_at_index(1)
    dll.print_list()
    print(dll.size)
    print(dll.get(1))
    # dll.prepend(7)
    # dll.prepend(2)
    # dll.prepend(1)
    # dll.add_at_index(3,0)
    # dll.delete_at_index(2)
    # dll.print_list()
    # print(dll.size)
    # dll.append(1)
    # dll.append(2)
    # dll.append(3)
    # dll.prepend(0)
    # print(f"Get element at index 1 {dll.get(1)}")
    # print("List after appending and prepending:")
    # dll.print_list()
    # dll.delete(2)
    # print("List after deleting 2:")
    # dll.print_list()
    # dll.add_at_index(2, 2)
    # print("List after readding 2")
    # dll.print_list()
    # dll.delete_at_index(3)
    # print("List after deleting at index 3")
    # dll.print_list()
