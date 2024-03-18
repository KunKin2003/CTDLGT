import sys
sys.path.append("./Buoi7")
from Stack import Stack

def StackMin(st):
    if st.LinkedList.head == None:
        return "Stack is Emty"
    else:
        min = st.LinkedList.head.value
        cur = st.LinkedList.head
        while cur:
            if cur.value < min:
                min = cur.value
            cur = cur.next

    return min

customStack = Stack()
print(customStack.isEmty())
customStack.push(9)
customStack.push(5)
customStack.push(4)
customStack.push(1)
customStack.push(8)
print(customStack.LinkedList)
print(StackMin(customStack))
