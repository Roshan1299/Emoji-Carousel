class Node:
    """A class representing a node in a circular doubly-linked list."""
    
    def __init__(self, data=None):
        """Initialize a node with optional data."""
        self.data = data
        self.next = None
        self.prev = None
        
    def get_data(self):
        """Get the data stored in the node."""
        return self.data

    def set_data(self, new_data):
        """Set the data stored in the node."""
        self.data = new_data

    def get_next(self):
        """Get the reference to the next node."""
        return self.next

    def set_next(self, new_next):
        """Set the reference to the next node."""
        self.next = new_next

    def get_prev(self):
        """Get the reference to the previous node."""
        return self.prev

    def set_prev(self, new_prev):
        """Set the reference to the previous node."""
        self.prev = new_prev
        
class CircularDoublyLinkedList:
    """A class representing a circular doubly-linked list."""
    MAX_size = 5   
    
    def __init__(self) :
        """Initialize an empty circular doubly-linked list."""
        self.head = None
        self.tail = None
        self.current = None
        self.length = 0
        self.Max_size = 5   

    def add_node(self, data,side):
        """Add a new node to the circular doubly-linked list."""
        if self.length >= self.Max_size:
            raise Exception("You cannot add emojis! Carousel is Full.")
        
        new_node = Node(data)
        if not self.head:
            # If the list is empty, add the first node
            self.head = new_node
            self.tail = new_node
            self.current = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # If the list is not empty, prompt the user to specify the location
            if side.upper() == 'LEFT':
                # Add the new node to the left of the current node
                new_node.prev = self.current.prev
                new_node.next = self.current
                self.current.prev.next = new_node
                self.current.prev = new_node
                if self.current == self.head:
                    self.head = new_node
            elif side.upper() == 'RIGHT':
                # Add the new node to the right of the current node
                new_node.prev = self.current
                new_node.next = self.current.next
                self.current.next.prev = new_node
                self.current.next = new_node
                if self.current == self.tail:
                    self.tail = new_node

        self.length += 1
        self.current = new_node

    def remove_node(self):
        """Remove the current node from the circular doubly-linked list."""
        if self.length == 0:
            raise Exception("List is empty")
        if self.length == 1:
            self.head = None
            self.tail = None
            self.current = None
        else:
            deleted_node = self.current
            if deleted_node == self.head:
                self.head = deleted_node.next
            if deleted_node == self.tail:
                self.tail = deleted_node.prev
            deleted_node.prev.next = deleted_node.next
            deleted_node.next.prev = deleted_node.prev
            self.current = deleted_node.prev  # Move current to the left of the deleted node
            del deleted_node
        self.length -= 1

    def get_current(self):
        """Get the data of the current node."""
        if self.current is None:
            raise Exception("List is empty")
        return self.current.data

    def get_prevs(self) :
        """Return the data of the node previous to the current node."""
        if self.current is None:
            raise Exception("List is empty")
        return self.current.get_prev().get_data()

    def get_nexts(self) :
        """Return the data of the node next to the current node."""
        if self.current is None:
            raise Exception("List is empty")
        return self.current.get_next().get_data()
    
    def move_next(self):
        """Move to the next node in the circular doubly-linked list."""
        if self.current is None:
            raise Exception("List is empty")
        self.current = self.current.next

    def move_prev(self):
        """Move to the previous node in the circular doubly-linked list."""
        if self.current is None:
            raise Exception("List is empty")
        self.current = self.current.prev