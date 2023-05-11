class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self):
        val = int(input("Insert the element in queue: "))
        if self.rear is None:
            self.rear = Node(val)
            self.front = self.rear
        else:
            temp = Node(val)
            self.rear.next = temp
            self.rear = temp

    def delete(self):
        if self.front is None:
            print("Underflow")
            return
        else:
            temp = self.front
            if temp.next is not None:
                temp = temp.next
                print("Element deleted from queue is: ", self.front.data)
                del self.front
                self.front = temp
            else:
                print("Element deleted from queue is: ", self.front.data)
                del self.front
                self.front = None
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        else:
            temp = self.front
            print("Queue elements are: ", end="")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

queue = Queue()
while True:
    print("1) Insert element to queue")
    print("2) Delete element from queue")
    print("3) Display all the elements of queue")
    print("4) Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        queue.insert()
    elif ch == 2:
        queue.delete()
    elif ch == 3:
        queue.display()
    elif ch == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")


'''
OUTPUT 

Enter your choice :
1
Insert the element in queue :
5
Enter your choice :
1
Insert the element in queue :
10
Enter your choice :
3
Queue elements are: 5 10
Enter your choice :
2
Element deleted from queue is : 5
Enter your choice :
3
Queue elements are: 10
Enter your choice :
4
Exit
'''
