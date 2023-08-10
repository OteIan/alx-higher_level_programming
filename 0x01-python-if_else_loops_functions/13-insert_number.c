#include "lists.h"

/**
 * insert_node - Inserts a node into a singly linked list
 *
 * @head: Double pointer to the head node of the list
 * @number: Number to be stored in the data(n) of the node
 *
 * Return: Address of the node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;

	return (new);
}
