#include <stdio.h>

int main(void)
{
    FILE *input = fopen("hi.txt", "r");
    printf("%p\n", input);

    char buffer[100];
    fread(buffer, 1, 3, input);
    // input : location to read from
    // 1 : size of blocks to read (in bytes)
    // 3 : how many blocks to read
    // buffer: location to store blocks

    // print the text
    printf("%s\n", buffer);
}