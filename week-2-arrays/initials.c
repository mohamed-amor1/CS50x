#include <stdio.h>

int main(int argc, char *argv[])
{
    for (int i = 0; i < argc; i++)
    {
        printf("Initials are %c and %c\n", argv[i + 1][i], argv[i + 2][i]);
        return 0;
    }
}