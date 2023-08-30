#!/usr/bin/python3
"""Node class and SinglyLinkedList class definition"""


class Node:
    """Represent a node in a singly linked list"""
    def __init__(self, data, next_node=None):
        """
        This initilazes a new node instance

        Args:
            data (int): Data stored by the node
            next_node (Node): The next node of the new node
        """
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """
        Getter method for data attribute

        Return:
            int: Data stored by the node
        """
        return self.__data

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
        return self.__next_node

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
        self.__next_node = value


class SinglyLinkedList:
    """This represents a singly linked list"""
    def __init__(self):
        """This initializes a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node to a singly linked list

        It is inserted at the correct numerical position based on the data

        Args:
            value (Node): The new node to insert
        """
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new
        else:
            current = self__.head
            while (current.next_node is not None or
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """This defines print() representation of a SinglyLinkedList"""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
