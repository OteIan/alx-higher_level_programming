#include "lists.h"

/**
 * check_cycle - Checks if a list has a cycle in it
 * 
 * @list: Pointer to the head node of the list
 * 
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
    listint_t *current = list, *checker = list->next;
    int n = 0, i, count = 0;

    while (current != NULL)
    {
        current = current->next;
        count++;
    }

    current = list;

    while (current != NULL)
    {
        checker = current->next;
        n = current->n;

        while (checker != NULL)
        {
            i = checker->n;
            if (n == i)
                return (1);
            checker = checker->next;
        }
    }

    return (0);
}