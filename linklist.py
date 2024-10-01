class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, head:Node = None, tail:Node = None) :
        self.head = head
        self.tail = tail
    
    def display(self):
        head = self.head
        while(head != None):
            print(str(head.data),  '->', end=" ")
            head = head.next
        print(None)
    
    def display_head(self):
        print(self.head.data)
    
    def display_tail(self):
        print(self.tail.data)

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            self.tail = current.next
        
    
    def insert_at_beginning(self, data):
        # check head is empty
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
    
    def insert_at_loc(self, data, loc):
        # check ll is empty
        if not self.head:
            self.head = Node(data)
        elif loc == 0:
            self.insert_at_beginning(data)
        else:
            pos = 0
            current = self.head
            while pos != loc - 1:
                current = current.next
                pos += 1
            
            new_node = Node(data)
            new_node.next, current.next = current.next, new_node
            if not new_node.next:
                self.tail = new_node
    
    def remove_at_begining(self):
        if not self.head:
            return
        self.head = self.head.next
    
    def remove_at_end(self):
        #import pdb; pdb.set_trace()
        if not self.head:
            return
        if self.head.next is None:
            self.head = self.tail = None
        current = self.head
        print(current)
        while current.next and current.next.next:
            current = current.next
            if current.next == self.tail:
                
                current.next = None
                self.tail = current
            
                
            
        
            
                
            

def main():
    ll = LinkedList()
    while(True):
        print("\n================= Welcome to Linked List Menu ==================\n")
        print(
            " \
            1. Insert a Node at End\n \
            2. Display Linked List\n \
            3. Insert a Node at Begining\n \
            4. Insert at Location\n \
            5. Display HEAD of Linked List\n \
            6. Display TAIL of Linked List\n \
            7. Remove a Node from beginning\n \
            8. Remove a Node from ending\n \
            9. Quit  \
            ")
        
        choice = int(input("\nEnter your choice \n"))
        match(choice):
            case 1:
                data = int(input("Enter Data:"))
                ll.insert_at_end(data)
                print("Data Inserted Successfully\n")
            case 2:
                ll.display()
            case 3:
                data = int(input("Enter Data:"))
                ll.insert_at_beginning(data)
                print("Data Inserted Successfully\n")
            case 4:
                data = list(map(int, input("Enter Data:").split(',')))
                ll.insert_at_loc(data[0], data[1])
                print("Data Inserted Successfully\n")
            case 5:
                ll.display_head()
            case 6:
                ll.display_tail()
            case 7:
                ll.remove_at_begining()
                print("Remove successfully")
            case 8:
                ll.remove_at_end()
                print("Removed from end")
            case 9:
                print("bubye...")
                return


if __name__ == '__main__':
    main()
    pass