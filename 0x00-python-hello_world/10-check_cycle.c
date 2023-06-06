#include "lists.h"

/**
 * check_cycle - spotting cycle
 * 
 * @list: head 
 * Return: zero if there is no cycle and 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next ==NULL)
		return (0);
	slow = list;
	fast = list->next;

	while(slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
