#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prevNode = NULL, *currNode = NULL, *nextNode = NULL;

	currNode = head;
	nextNode = head->next;
	while (currNode != NULL)
	{
		nextNode = currNode->next;
		currNode->next = prevNode;
		prevNode = currNode;
		currNode = nextNode;
	}
	head = prevNode;
	return (head);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}

	slow = reverse_list(slow);
	fast = *head;

	while (slow != NULL)
	{
		if (fast->n != slow->n)
			return (0);

		slow = slow->next;
		fast = fast->next;
	}

	return (1);
}
