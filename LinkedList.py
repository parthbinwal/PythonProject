class Node:
    # Linked List Structure ex:[9|-]-->[11|None]
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    #first time creating obj head will point to none
    def __init__(self):
        self.head=None


    def insertAtBeginning(self,value):
        if self.head is None :
            node=Node(value)
            self.head=node



