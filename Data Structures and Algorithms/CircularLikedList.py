class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        val = self.head
        while val.next:
            if val.next == self.head:
                break
            val = val.next
        newNode = Node(data, self.head)
        self.head = newNode
        val.next = newNode

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        val = self.head
        while val.next:
            if val.next == self.head:
                val.next = Node(data, self.head)
                break
            val = val.next

        val.next = Node(data, self.head)

    def insert_all(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_end(i)

    def print_all(self):
        if self.head is None:
            return None
        val = self.head
        ans = ''
        while val:

            ans += str(val.data)+'---->' if val.next else str(val.data)
            if val.next == self.head:
                break
            val = val.next
        print(ans)

    def print_from(self, fr):
        val = self.head
        ans = ''
        while val:
            if val.data == fr:
                while val.next.data != fr:
                    ans += str(val.data) + '---->'
                    val = val.next
                ans += str(val.data)
                break
            val = val.next

        print(ans)


if __name__ == '__main__':
    c = CircularLinkedList()
    c.insert_all([1, 2, 3, 4])
    c.print_all()
    c.insert_beg(6)
    c.print_all()
    c.insert_end(9)
    c.print_all()
    c.print_from(2)
