class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LikedList:
    def __init__(self):
        self.head = None

    def print_all(self):
        if self.head is None:
            return None

        val = self.head
        ele = ''
        while val:
            ele += str(val.data)+'--->' if itr.next else str(val.data)

            val = val.next
        print(ele)

    def get_length(self):
        c = 1
        val = self.head
        while val.next:
            count += 1
            val = val.next
        return count

    def insert_beg(self, data):

        newNode = Node(data, self.head)
        self.head = newNode

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        val = self.head
        while val.next:
            val = val.next

        val.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            return self.insert_beg(data)

        c = 0
        val = self.head
        while val:
            if c == index-1:
                newNode = Node(data, val.next)
                val.next = newNode
                break
            val = val.next
            c += 1


if __name__ == '__main__':
    lt = LikedList()
    lt.head = Node(1)
