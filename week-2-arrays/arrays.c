#include <stdio.h>
#include <math.h>

int main(void)
{
    unsigned int length;
    do
    {
        printf("Enter the size of the array:\n");
        scanf("%d", &length);
    } while (length < 1);

    printf("You entered the size: %d\n", length);

    int twice[length];
    twice[0] = 1;

    int i;

    for (i = 1; i < length; i++)
    {
        twice[i] = twice[i - 1] * 2;
        // or  twice[i] = 1 << i;
    }

    printf("Powers of 2:\n");

    for (i = 0; i < length; i++)
    {
        printf("%d\n", twice[i]);
    }

    return 0;
}
