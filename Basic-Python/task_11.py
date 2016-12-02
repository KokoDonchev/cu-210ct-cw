"""
Week 5 Task 2

Based on the Python code or the C++ code provided in class as a starting point,
implement the double linked list node delete function.

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, n, x):
        # Not actually perfect: how do we prepend to an existing list?
        if n != None:
            x.next = n.next
            n.next = x
            x.prev = n
            if x.next != None:
                x.next.prev = x
        if self.head == None:
            self.head = self.tail = x
            x.prev = x.next = None
        elif self.tail == n:
            self.tail = x

    def display(self):
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next
        print("List: ", ",".join(values))

    def delete(self, y):
        """
        When we are working with double linked lists, we don't delete
        the actual value, we remove its pointer! a.k.a index
        """

        cn = self.head  # our current node

        while cn is not None:
            if cn.value == y:
                if cn.prev is not None:
                    cn.prev.next = cn.next
                    cn.next.prev = cn.prev
                else:
                    self.head = cn.next
                    cn.next.prev = None

            cn = cn.next

if __name__ == '__main__':
    l = List()
    l.insert(None, Node(4))
    l.insert(l.head, Node(6))
    l.insert(l.head, Node(8))
    l.display()
    print('----')
    l.delete(4)
    l.display()