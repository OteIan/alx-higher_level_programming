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
	listint_t *turtle, *hare;
	listint_t *next = NULL, *prev = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	turtle = hare = *head;
	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		next = turtle->next;
		turtle->next = prev;
		prev = turtle;
		turtle = next;
	}

	if (hare != NULL)
		turtle = turtle->next;

	while (turtle != NULL)
	{
		if (turtle->n != prev->n)
			return(0);
		turtle = turtle->next;
		prev = prev->next;
	}
	return (1);
}
