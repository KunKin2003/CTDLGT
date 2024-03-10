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

    def middleNode(self):
        cur = self.head
        if self.length == 0 or self.length == 1:
            return None
        else:
            for _ in range(self.length//2 - 1):
                cur = cur.next
            middle_node = cur.next
        return middle_node.value
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
new_linked_list = LinkedList()
new_linked_list.append(5)
new_linked_list.append(10)
new_linked_list.append(15)
new_linked_list.append(18)
new_linked_list.append(12)
new_linked_list.append(11)
new_linked_list.append(6)
print(new_linked_list.__str__())
print(new_linked_list.middleNode())
        