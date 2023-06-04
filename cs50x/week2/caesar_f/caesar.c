#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

string cipher(string text, int key);

int main(int argc, string argv[])
{
    int key = atoi(argv[1]);

    if(argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if(key < 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    string text = get_string("plaintext:  ");

    cipher(text, key);

    printf("ciphertext: %s\n", text);
}


string cipher(string text, int key)
{
    for(int i = 0; i < strlen(text); i++)
    {
        int i_char = text[i];

        if((i_char > 64 && i_char < 91))
        {
            int c_char = i_char + key;

            if(c_char > 91)
            {
                c_char = 65 + ((i_char + key) % 26);
            }
            else
            {
                c_char += 0;
            }

            char ci_char = c_char;
            text[i] = ci_char;
        }
        else if((i_char > 96 && i_char < 123))
        {
            int c_char = i_char + key;

            if(c_char > 123)
            {
                c_char = 97 + ((i_char + key) % 26);
            }
            else
            {
                c_char += 0;
            }

            char ci_char = c_char;

            text[i] = ci_char;
        }
        else
        {
            int c_char = i_char;
            char ci_char = c_char;
            text[i] = ci_char;
        }
    }
    return text;
}