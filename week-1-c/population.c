#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
    // Prompting the user for a starting # of llamas
    int start;
    do
    {
        printf("Start size: ");
        scanf("%d", &start);
    } while (start < 9);

    // Prompting the user for an ending # of llamas
    int end;
    do
    {
        printf("End size: ");
        scanf("%d", &end);
    } while (end < start);

    // How many years to reach end size
    int y;
    double s = (double)start;
    double e = (double)end;
    double s_trunc = 0;

    while (s < e)
    {
        s = round(s + (s / 3) - (s / 4));
        y = y + 1;
    }
    printf("Years: %d\n", y);

    system("pause");
    return 0;
}