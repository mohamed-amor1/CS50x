#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[] = "Emma";
    int length = strlen(name);
    int i;

    for (i = 0; i < length; i++)
    {
        printf("%c \n", name[i]);
        // or printf("%d \n", name[i]); if we want to print ASCII of each character
    }
}