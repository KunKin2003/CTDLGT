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
    
    def mergeLinkedList(self, l1, l2):
        l = l1 + l2
        if len(l) not in range(50):
            raise Exception("Sorry, The number of nodes in both lists is in the range [0, 50].")
        for ele in l:
            if -100 >= ele or ele >= 100:
                raise ValueError("Sorry, -100 <= Node.val <= 100")
        l.sort()
        for element in l:
            self.append(element)
        
new_linked_list = LinkedList()
list1 = [1,2,4]
list2 = [4,1,5,9,1]
new_linked_list.mergeLinkedList(list1, list2)
print(new_linked_list.__str__())

