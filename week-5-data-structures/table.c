#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a struct to represent a node in a linked list
typedef struct node
{
    char phrase[500];
    struct node *next;
} node;

// Define an array of linked lists, one for each letter of the alphabet
node *table[26];

// TODO: return an index, 0–25, for a given phrase
int hash(char phrase[]);

int main(void)
{
    // Loop three times
    for (int i = 0; i < 3; i++)
    {
        // Prompt the user to enter a phrase
        char phrase[500];
        printf("Enter a new phrase: ");
        scanf("%s", phrase);

        // Hash the phrase to get an index into the table
        int index = hash(phrase);

        // Print the original phrase and its hash index
        printf("%s hashes to %i\n", phrase, index);
    }
}

// This function hashes a given phrase to an index in the table
int hash(char phrase[])
{
    // Convert the first character of the phrase to uppercase and subtract 'A'
    // to get an index from 0 to 25
    return toupper(phrase[0]) - 'A';

    // A = 65
    // A - A = 0
    // B - A = 1
    // Z - A = 25
}
