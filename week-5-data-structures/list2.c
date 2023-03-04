#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    char phrase[500];
    struct node *next;
} node;

#define LIST_SIZE 2

void unload(node *list);
void visualize(node *list);

int main(void)
{
    node *list = NULL;

    // This code creates a linked list and adds items to it by dynamically allocating memory for new nodes and adding them to the beginning of the list.
    for (int i = 0; i < LIST_SIZE; i++)
    {
        printf("Enter a new phrase: ");
        char phrase[500];
        scanf("%s", phrase);

        // add phrase to new node in list
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Couldn't allocate memory for node\n");
            return 1;
        }
        strcpy(n->phrase, phrase);
        n->next = list;

        list = n;

        // Visualize list after adding a node.
        visualize(list);
    }

    unload(list);
}

void unload(node *list)
{
    // Free all allocated nodes
    while (list != NULL)
    {
        node *ptr = list->next;
        free(list);
        list = ptr;
    }
}

void visualize(node *list)
{
    printf("\n+-- List Visualizer --+\n\n");
    while (list != NULL)
    {
        printf("Location %p\n", list);
        printf("Phrase: \"%s\"\n", list->phrase);
        printf("Next: %p\n\n", list->next);
        list = list->next;
    }
    printf("+---------------------+\n\n");
}