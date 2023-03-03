#include <stdio.h>

int factorial(int number);

int main(void)
{
    int n;
    // Prompt the user for a number
    printf("Enter a positive integer to compute its factorial: ");
    scanf("%d", &n);
    printf("The factorial of %d is: %d\n", n, factorial(n));
}

int factorial(int number)
{
    if (number == 1)
    {
        return 1;
    }

    return number * factorial(number - 1);

    // int solution = 1;
    // int coef;
    // for (int i = 1; i <= number; i++)
    // {
    //     coef = number - number + i;
    //     solution = coef * solution;
    // }
    // return solution;

    // or

    // int result = 1;
    // for (int i = 2; i <= number; i++)
    // {
    //     result *= i;
    // }

    // return result;
}