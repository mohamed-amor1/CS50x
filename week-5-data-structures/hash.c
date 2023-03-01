#include <stdio.h>
#include <stdlib.h>

#define LONGEST_WORD 45
#define NUMBER_OF_BUCKETS 26

typedef struct node
{
    char word[LONGEST_WORD + 1];
    struct node *next;
} node;

// Trie
typedef struct node
{
    bool is_word;
    struct node *children[SIZE_OF_ALPHABET];
} node;

int main(void)
{
    node *hash_table[NUMBER_OF_BUCKETS];
}