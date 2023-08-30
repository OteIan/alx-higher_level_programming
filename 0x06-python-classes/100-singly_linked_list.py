#!/usr/bin/python3
"""Node class and SinglyLinkedList class definition"""


class Node:
    """
    This defines a node based one the provided data and next node object

    Attributes:
        __data (int): Data to be help by the node (Private attribute)
        __next_node (Node object): Pointer to the next node
    """
    def __init__(self, data, next_node=None):
        """
        This initilazes a new node instance

        Args:
            data (int): Data stored by the node
            next_node (Node object): Pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def

class SinglyLinkedList:
    """
    """
