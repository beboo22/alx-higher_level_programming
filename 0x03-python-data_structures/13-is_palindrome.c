#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to pointer to head node
 *
 * Return: 1 if linked list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp2;
	int *arr;
	int nnode, i, j;

	temp2 = *head;
	nnode = 0;
	if (temp2 != NULL)
	{
		while (temp2 != NULL)
		{
			temp2 = temp2->next;
			nnode++;
		}
	}
	temp2 = *head;
	arr = malloc(nnode * sizeof(int));
	i = 0;
	while (temp2 != NULL)
	{
		arr[i] = temp2->n;
		temp2 = temp2->next;
		i++;
	}
	for (i = 0, j = nnode - 1; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
