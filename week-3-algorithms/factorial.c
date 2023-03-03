#include <stdio.h>

int factorial(int number);

int main(void)
{
    int n;
    int result;
    // Prompt the user for a number
    printf("Enter a positive integer to compute its factorial: ");
    scanf("%d", &n);
    result = factorial(n);
    printf("The factorial of %d is: %d\n", n, result);
}

int factorial(int number)
{
    if (number == 1)
    {
        return 1;
    }

    return number * factorial(number - 1);
}