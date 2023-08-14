#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * 
 * @head: Double pointer to the head node of the list
 * 
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int count = 0;

    if (head == NULL || *head == NULL)
        return (1);

    while (current != NULL)
    {
        count++;
        current = current->next;
    }

    
}