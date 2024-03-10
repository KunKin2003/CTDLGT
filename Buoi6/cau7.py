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

    def removeDuplicates(self):
        my_list = []
        cur = self.head
        while cur.next:
            if cur.next.value not in my_list:
                my_list.append(cur.next.value)
            else:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = None
                continue
            cur = cur.next
        print(my_list)

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
new_linked_list.append(15)
new_linked_list.append(6)
new_linked_list.append(12)
print(new_linked_list.__str__())
new_linked_list.removeDuplicates()
print(new_linked_list.__str__())
