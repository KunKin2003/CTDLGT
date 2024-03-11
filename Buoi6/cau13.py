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
    
    def middleNode(self):
        tmp = tmp1 = self.head
        while tmp1 and tmp1.next:
            tmp = tmp.next
            tmp1 = tmp1.next.next
        return tmp.value

new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(3)
new_linked_list.append(8)
new_linked_list.append(2)
new_linked_list.append(5)
new_linked_list.append(9)
new_linked_list.append(8)

print(new_linked_list.__str__())
print(new_linked_list.middleNode())