#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

const int HEADER_SIZE = 44;
int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input);

    // Use check_format to ensure WAV format
    // TODO #4
    if(check_format(header) == 1)
    {
        printf("Not a valid wav filee.\n");
        return 1;
    }

    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&header, sizeof(WAVHEADER), 1, output);

    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(header);

    // Write reversed audio to file
    // TODO #8
    BYTE buffer;
    fseek(input, 0, SEEK_END);
    long audio_size = ftell(input) - HEADER_SIZE;
    fseek(input, -1 * block_size, SEEK_END);

    for(long i = 0; i > HEADER_SIZE; i-=block_size)
    {
        fread(&buffer, block_size, 1, input);
        fwrite(&buffer, block_size, 1, output);
        fseek(input, -2 * block_size, SEEK_CUR);
    }

    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if(header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 0;
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int i = header.numChannels * header.bitsPerSample / 8;
    return i;
}