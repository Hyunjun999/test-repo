class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
class Node:
    def __init__(self, num, next = None) -> None:
        self.num = num
        self.next = next

def insert(self, n):
    new = Node(n)
    if self.head:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new
    else:
        self.head = new
l = LinkedList()
l.head = Node(3)
print(l.head.num)
