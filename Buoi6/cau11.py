class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
def reverseLinkedList(head):
    prev = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    
    return prev

new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(3)
new_linked_list.append(8)
new_linked_list.append(2)
new_linked_list.append(5)
new_linked_list.append(9)
new_linked_list.append(8)
new_linked_list.append(2)
print(new_linked_list.__str__())
new_linked_list.head = reverseLinkedList(new_linked_list.head)
print(new_linked_list.__str__())

