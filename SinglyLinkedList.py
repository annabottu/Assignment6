class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
    
    def delete(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if not curr:
            return
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next
    
    def traverse(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements


ll = SinglyLinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print("Linked List:", ll.traverse())
ll.delete(20)
print("After deletion:", ll.traverse())
