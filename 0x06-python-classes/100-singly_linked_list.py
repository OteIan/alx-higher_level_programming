#!/usr/bin/python3
"""Node class and SinglyLinkedList class definition"""


class Node:
    """
    This defines a node based one the provided data and next node object

    Attributes:
        __data (int): Data to be help by the node (Private attribute)
        __next_node (Node): Pointer to the next node (Private attribute)
    """
    def __init__(self, data, next_node=None):
        """
        This initilazes a new node instance

        Args:
            data (int): Data stored by the node
            next_node (Node): Pointer to the next node (Default is None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data attribute

        Return:
            int: Data stored by the node
        """
        return self.data
    
    @data.setter
    def data(self, value):
        """
        Setter method for data attribute

        Args:
            value (int): Data stored by the node
        
        Raises:
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
        
    @property
    def next_node(self):
        """
        Getter method for next_node attribute

        Return:
            Node: Pointer to the next node
        """
        return self.next_node
    
    @next_node.setter
    def next_node(self, value):
        """
        Setter methos for next_node attribute

        Args:
            value (Node): Pointer to the next node
        
            Raises:
                TypeError: If value is not a node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a node abject")
        self.__next.node = value

class SinglyLinkedList:
    """
    This defines a SinglyLinkedList based on the provided nodes

    Attribute:
        __head (Node): Pointer to the head node of the list
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        This defines a new sorted_insert instance

        Args:
            value (int): Value to be stored by the node
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next_node is not None or current.next_node.data < value:
            current = current.next_node
        
        new_node.next_node = current.next_node
        current.next_node = new_node