#include <stdio.h>

int main(void)
{
    int a = 28;
    int b = 50;
    int *c = &a;

    *c = 14; // Go to where c is pointing and change the value to 14.
    c = &b;
    *c = 25;

    printf("a has the value %d, located at %p\n", a, (void *)&a);
    printf("b has the value %d, located at %p\n", b, (void *)&b);
    printf("c has the value %p, located at %p\n", c, (void *)&c);

    return 0;
}