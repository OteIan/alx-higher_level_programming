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
    listint_t *turtle, *hare;
    int count = 0;
  
    if (head == NULL || *head == NULL)
        return (1);

    turtle = hare = *head;
    while (current != NULL)
    {
        current = current->next;
        count++;
    }
    while (hare != NULL)
    {
        turtle = turtle->next;
        hare = hare->next->next;
    }
    
    turtle = reverse_list(turtle);
    current = *head;
    while (current != NULL && turtle != NULL)
    {
        if (current->n == turtle->n)
        {
            current = current->next;
            turtle = turtle->next;
            continue;
        }
        else
            break;
    }
    /* Return 1 if both current and turtle are NULL, else return 0 */
    return (current == NULL && turtle == NULL);
}

/**
 * reverse_list - Reverses a singly linked list
 * 
 * @head: Pointer to the head node of the list
 * 
 * Return: Pointer to the head node of the reversed list
*/
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *next = NULL;
    listint_t *current = head;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;

        prev = current;
        current = next;
    }

    return (prev);
}