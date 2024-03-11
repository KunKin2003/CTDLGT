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
    
def mergeTwoLists(list1,list2):
    tmp = Node(None)
    cur = tmp

    while list1 and list2:
        if list1.value <  list2.value:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 if list1 else list2
    
    return tmp.next

new_linked_list1 = LinkedList()
new_linked_list1.append(2)
new_linked_list1.append(3)
new_linked_list1.append(4)
new_linked_list1.append(5)
new_linked_list1.append(9)

new_linked_list2 = LinkedList()
new_linked_list2.append(3)
new_linked_list2.append(4)
new_linked_list2.append(6)
new_linked_list2.append(7)

print(new_linked_list1.__str__())
print(new_linked_list2.__str__())
merge_head = mergeTwoLists(new_linked_list1.head,new_linked_list2.head)
while merge_head:
    print(merge_head.value, end="")
    if merge_head.next:
        print("->",end="")
    merge_head = merge_head.next







