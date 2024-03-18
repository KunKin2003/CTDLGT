class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return '->'.join(values)
    
    def enqueue(self, value):
        node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    def isEmpty(self):
        return self.linkedList.head == None
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tmpNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next

            return tmpNode

    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.head = None

cusQueue = Queue()
cusQueue.enqueue(1) 
cusQueue.enqueue(2) 
cusQueue.enqueue(3) 
print(cusQueue)
print(cusQueue.peek())
print(cusQueue)
print(cusQueue.dequeue().value)
print(cusQueue)
