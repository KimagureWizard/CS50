#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit[]);

int convert(int byte, int bit[]);

int main(void)
{
    // TODO

    string message = get_string("Type in:  ");

    for(int e = 0; e < strlen(message); e++)
    {
        int byte = message[e];

        int bit[BITS_IN_BYTE];

        convert(byte, bit);

        print_bulb(bit);

        printf("\n");
    }
}

void print_bulb(int bit[])
{
    for(int i = BITS_IN_BYTE - 1; i >= 0; i--)
    {
        if (bit[i] == 0)
        {
            // Dark emoji
            printf("\U000026AB");
        }
        else if (bit[i] == 1)
        {
            // Light emoji
            printf("\U0001F7E1");
        }
    }
}

int convert(int byte, int bit[])
{
    for(int c = 0; c < BITS_IN_BYTE; c++)
    {
        bit[c] = byte % 2;
        byte /= 2;
    }
    return 0;
}