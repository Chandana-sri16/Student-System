# charan's module
# developed linked lists

class Node:
    def __init__(self):
        global a, b, c, d, e
        a = input("Enter student name: ")
        b = input("Enter Roll no: ")
        c = input("Enter College name: ")
        d = input("Email ID: ")
        e = input("Course name: ")
        self.data = a, b, c, d, e
        self.Next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.Next is None:
                    break
                lastNode = lastNode.Next
            lastNode.Next = newNode

    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(list(currentNode.data))
            currentNode = currentNode.Next


# firstnode = Node()
# linkedlist = LinkedList()
# linkedlist.insert(firstnode)
# linkedlist.printlist()


