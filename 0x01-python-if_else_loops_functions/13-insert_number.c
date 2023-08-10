#include "lists.h"

/**
 * insert_node - Inserts a node into a singly linked list
 *
 * @head: Double pointer to the head node of the list
 * @number: Number to be stored in the data(n) of the node
 * @index: Index at which the node is to be inserted
 *
 * Return: Address of the node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number, int index)
{
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));
	int i = 0;

	if (head == NULL || *head == NULL || new == NULL)
		return (NULL);

	new->n = number;
	if (index == 0)
	{
		if (current->next != NULL)
			new->next = current->next;
		current = new;
	}
	while (current != NULL)
	{
		if (i == index - 1)
		{
			if (current->next != NULL)
				new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
		i++;
	}
	return (NULL);
}
