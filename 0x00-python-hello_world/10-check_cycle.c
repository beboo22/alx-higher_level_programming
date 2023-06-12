#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *temp2;

	temp = list;
	temp2 = list;

	while (temp2 != NULL && temp2->next != NULL)
	{
		temp2 = temp2->next->next;
		if (temp2 == temp)
			return (1);
		temp = temp->next;
	}

	return (0);
}
