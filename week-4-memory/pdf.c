#include <stdio.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Improper usage.");
        return 1;
    }

    // Open file
    char *filename = argv[1];
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {
        printf("No such file found.\n");
        return 1;
    }

    uint8_t buffer[4];
    uint8_t signature[] = {37, 80, 68, 70};

    // File handling code here

    fread(buffer, 1, 4, file);

    for (int i = 0; i < 4; i++) // we're printing what's inside buffer
    {
        printf("%d ", buffer[i]);
    }
    printf("\n");

    // Method 1
    // if ((buffer[0] == 37) && (buffer[1] == 80) && (buffer[2] == 68) && (buffer[3] == 70))
    // {
    //     printf("Likely a PDF!\n");
    // }
    // else
    // {
    //     printf("Likely not a PDF!\n");
    // }

    // Method 2
    for (int i = 0; i < 4; i++)
    {
        if (buffer[i] != signature[i])
        {
            printf("Likely not a PDF!\n");
            return 0;
        }
    }
    printf("Likely a PDF!\n");

    // Close file

    fclose(file);

    return 0;
}