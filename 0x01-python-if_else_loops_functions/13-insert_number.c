#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list
 * @head: pointer to the head
 * @number: number to insert
 * Return: a pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    listint_t *current;

    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || (*head)->n >= number) {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    current = *head;

    while (current->next != NULL && current->next->n < number) {
        current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}
