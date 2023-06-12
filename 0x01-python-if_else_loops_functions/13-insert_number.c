#include "lists.h"

/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: pointer to pointer to head node
 * @number: value to insert into list
 *
 * Return: pointer to new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *nnode;
	int idx;

	nnode = malloc(sizeof(listint_t));
	if (nnode == NULL)
		return (NULL);

	idx = number;
	temp = *head;
	while (temp != NULL && temp->n < idx)
	{
		temp = temp->next;
	}

	nnode->n = idx;
	nnode->next = temp;
	if (*head == NULL || idx < (*head)->n)
		*head = nnode;
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < idx)
		{
			temp = temp->next;
		}
		nnode->next = temp->next;
		temp->next = nnode;
	}

	return (nnode);
}
