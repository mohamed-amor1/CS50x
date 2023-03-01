#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[50];
    int age;
    long number;

    printf("Enter your name: ");
    scanf("%s", name);

    printf("What's your age: ");
    scanf("%d", &age);

    printf("Enter your phone number: ");
    scanf("%ld", &number);

    printf("Name is %s. Age is %d. Phone number is %ld\n", name, age, number);

    return 0;
}