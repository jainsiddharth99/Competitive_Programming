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
            ele += str(val.data)+'--->' if val.next else str(val.data)

            val = val.next
        print(ele)

    def get_length(self):
        count = 1
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

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return

        c = 0
        val = self.head
        while val:
            if c == index-1:
                val.next = val.next.next
                break

            val = val.next
            c += 1

    def insert_values(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_end(i)


if __name__ == '__main__':
    lt = LikedList()
    lt.insert_values([1, 2, 3, 4])
    lt.print_all()
    lt.insert_beg(5)
    print('inserting 5 in beg')
    lt.print_all()
    print('inserting 6 in end')
    lt.insert_end(6)
    lt.print_all()
    print('inserting --"Word" at index 3 --')
    lt.insert_at(3, 'Word')
    lt.print_all()
    print('removing satrting word')
    lt.remove_at(0)
    lt.print_all()
    print('removing index 2')
    lt.remove_at(2)
    lt.print_all()
    print('get length of ll')
    print(lt.get_length())

    print('removing index 4 -- currently last index')
    lt.remove_at(4)
    lt.print_all()
