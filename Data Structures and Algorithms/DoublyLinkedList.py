class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            return None
        val = self.head
        dll = ""
        while val:
            dll += str(val.data) + '---->' if val.next else str(val.data)
            val = val.next
        print(dll)

    def print_backward(self):
        if self.head is None:
            return None

        val = self.head
        while val.next:
            val = val.next
        dll = ""
        while val:
            dll += str(val.data) + '---->' if val.prev else str(val.data)
            val = val.prev
        print(dll)

    def get_length(self):
        c = 1
        val = self.head
        while val.next:
            c += 1
            val.next
        return c

    def insert_beg(self, data):
        # so here we are making a new node and setting
        # its next node to the current head
        newNode = Node(data, self.head, None)
        # now making head the new node
        self.head.prev = newNode
        self.head = newNode

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        val = self.head
        while val.next:
            val = val.next

        val.next = Node(data, None, val)

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            return self.insert_beg(data)

        c = 0
        val = self.head
        while val:
            if c == index-1:
                newNode = Node(data, val.next, val)
                if newNode.next:
                    newNode.next.prev = newNode
                val = val.next

                break

            val = val.next
            c += 1

    def insert_all(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_end(i)


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.insert_all([1, 2, 3, 4])
    d.print_forward()
    d.print_backward()
    d.insert_at(6)
    d.print_forward()
