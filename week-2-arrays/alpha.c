#include <stdio.h>
#include <string.h>

int main(void)
{
    char word[50];
    int i;

    printf("Enter a word: ");
    scanf("%s", word);
    printf("%s\n", word);

    int len = strlen(word);

    for (i = 0; i < len; i++)
    {
        if ((word[i] > 96) && (word[i] < 122))
        {
            if (word[i] < word[i + 1])
            {
                printf("Your text is in alphabetical order\n");
            }
            else
            {
                printf("your text is not in alphabetical order\n");
            }
        }
        else
        {
            printf("Your word is not in lowercase\n");
        }
    }
}