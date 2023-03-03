#include <stdio.h>
#include <string.h>

// Define a struct called "candidate" with name and votes attributes
typedef struct candidate
{
    char name[500];
    int votes;
} candidate;

// Declare a function called "get_candidate" that returns a candidate
candidate get_candidate(char prompt[500]);

int main(void)
{
    int n;
    printf("How many candidates are in this election?: ");
    scanf("%d", &n);

    candidate candidates_array[n];
    candidate temp[1];
    printf("Enter every candidate's attributes below\n");

    for (int i = 0; i < n; i++)
    {
        candidates_array[i] = get_candidate("Enter details\n");
    }

    // order by votes using bubble sort
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (candidates_array[i].votes < candidates_array[j].votes ||
                (candidates_array[i].votes == candidates_array[j].votes &&
                 strcmp(candidates_array[i].name, candidates_array[j].name) > 0))
            {
                temp[0] = candidates_array[i];
                candidates_array[i] = candidates_array[j];
                candidates_array[j] = temp[0];
            }
        }
    }

    // Print the name and votes of "candidates"
    for (int i = 0; i < n; i++)
    {
        printf("Candidate number %d: %s\n", i + 1, candidates_array[i].name);
        printf("Votes of candidate %d: %d\n", i + 1, candidates_array[i].votes);
    }

    return 0;
}

// Define the "get_candidate" function
candidate get_candidate(char prompt[500])
{
    printf("%s", prompt);

    // Declare a candidate variable "c"
    candidate c;

    // Prompt the user to enter a name and votes for the candidate and read them in
    printf("Enter a name: ");
    scanf("%s", c.name); // No need to use "&" operator with arrays

    printf("Enter a number of votes: ");
    scanf("%d", &c.votes); // Use "&" operator with integers

    // Return the candidate variable "c"
    return c;
}
