#include <stdio.h>
#include <stdlib.h>
#include <list.h>

/**
 * print_listint - element of a listint_t list printed
 * @h: pointer to head list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}

/**
 * add_nodeint_end - adds new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_list
 * @n: integer to be included in the new node
 * Return: address of new node element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
	*head = new;
	else
	{
	while (current->next != NULL)
	current = current->next;
	current->next = new;
	}
	return (new);
}

/**
 * free_listint - listint_t list freed
 * @head: list to freed pointer
 * Return: void
 */
void free_listint(listint_t *head)
{
	list_t *current;

	while (head != NULL)
	{
	current = head;
	head = head->next;
	free(current);
	}
}

