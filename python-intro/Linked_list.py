class Node:
    """Tugun obeykti"""
    def __init__(self,data):
        self.data=data
        self.next= None

class Linkedlist:
    """Linked list"""

    def __init__(self):
        self.head = None

    def printlist(self):
        temp =  self.head
        while temp:
            print(temp.data)
            temp =  temp.next
            
    def push(self, new_data):
        """Listni boshiga qiymat qoshish"""

        new_node=Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def insertafter(self,prev_node,new_data):
        """Biror tugundan keyin yangi tugun qoshish"""

        if prev_node is None:
            print("Tugun mavjud emas!")

        new_node=Node(new_data)

        new_node.next = prev_node.next

        pprev_node = new_node

    def append(self,new_data):
        """Oxriga yangi qiymat qoshish"""

        new_node=Node(new_data)
        last = self.head

        if self.head is None:

            self.head=new_node
            return

        
        while last.next:
            last=last.next
        last.next=new_node

    def deleteNode(self,key):

        temp=self.head

        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev =  temp
            temp = temp.next

        if temp == None:
            return
        prev.next = temp.next
        temp = None
        
