# OSL 02/12/2021

# implement a queue with linked list
# what is a queue?
# Think aobout people waiting in line. First come first serve (go).
# Dequeue: Remove the first in line.
# Enqueue: Add an element to the end of the queue.

class node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class queue():
    def __init__(self) -> None:
        self.head = node("Head")
        self.size = 0

    def printQueue(self):
        if self.size == 0:
            print("Empty queue!")
        else:
            front = self.head.next
            while front:
                print(front.value)
                front = front.next
    
    def enqueue(self, value):
        if self.size == 0:
            self.head.next = node(value)
        else:
            cur = self.head.next
            while cur.next:
                cur = cur.next
            cur.next = node(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return("Nothing to dequeue.")
        else:
            d = self.head.next
            self.head.next = d.next
            self.size -= 1
            return d.value




if __name__ == "__main__":
    myq = queue()
    for i in range(3):
        myq.enqueue(i)
    myq.printQueue()

    for _ in range(4):
        print('Dequeued:', myq.dequeue())