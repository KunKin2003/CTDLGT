class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def isEmty(self):
        return self.LinkedList.head == None
    
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmty():
            return None
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmty():
            return None
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None
    
def main():
    customStack = Stack()
    print(customStack.isEmty())
    customStack.push(1)
    customStack.push(2)
    customStack.push(3)
    customStack.push(4)
    print(customStack.LinkedList)
    print(customStack.pop())
    customStack.delete()
    print(customStack.LinkedList)

if __name__ == "__main__":
    main()
