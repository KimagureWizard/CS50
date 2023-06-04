#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
const int block_size = 512;
BYTE buffer[block_size];
int isJpeg(BYTE buffer[]);
int isSlack(BYTE buffer[]);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    int output_counter = 0;

    while(fread(&buffer, 1, block_size, input) == block_size)
    {
        if (isJpeg(buffer) == 1)
        {
            do
            {
                char filename[8];
                sprintf(filename, "%03i.jpg", output_counter);
                FILE *output = fopen(filename, "w");
                fwrite(&buffer, block_size, 1, output);
                output_counter++;
                fclose(output);
            }
            while(isSlack(buffer) == 0);
        }
    }

    fclose(input);
}

int isJpeg(BYTE buffer[])
{
    if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isSlack(BYTE buffer[])
{
    if(buffer[0] == 0x00 && buffer[1] == 0x00 && buffer[2] == 0x00 && buffer[3] == 0x00)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}