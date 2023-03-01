#include <stdio.h>

int main()
{
    int hours[5];
    int i;

    printf("Enter how many hours have you slept:\n");

    for (i = 0; i < 5; i++)
    {
        printf("Value %d: ", i + 1);
        scanf("%d", &hours[i]);
    }

    printf("You entered the following values:\n");

    for (i = 0; i < 5; i++)
    {
        printf("%d\n", hours[i]);
    }

    return 0;
}
