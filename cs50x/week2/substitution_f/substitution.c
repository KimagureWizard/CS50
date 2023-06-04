#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int distance(int key_list[]);

string cipher(string text, int key_list[]);

int main(int argc, string argv[])
{
    string key = argv[1];

    int key_list[26];

    for(int i = 0; i < 26; i++)
    {
        int c = tolower(key[i]);

        key_list[i] = c;
    }

    if(argc != 2 || strlen(key) != 26)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    for(int i = 0; i < strlen(key); i++)
    {
        char c = key[i];

        if(isalpha(c) == false)
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    }

    distance(key_list);

    string text = get_string("plaintext:  ");

    cipher(text, key_list);

    printf("ciphertext: %s\n", text);
}



int distance(int key_list[])
{
    int alpha[] = {97, 98 ,99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122};

    for(int i = 0; i < 26; i++)
    {
        key_list[i] -= alpha[i];
    }
    return 0;
}


string cipher(string text, int key_list[])
{
    for(int i = 0; i < strlen(text); i++)
    {
        int c = text[i];

        if(islower(text[i]))
        {
            c += key_list[c-97];
            text[i] = c;
        }
        else if(isupper(text[i]))
        {
            c += key_list[c-65];
            text[i] = c;
        }
        else
        {
            text[i] = c;
        }
    }
    return text;
}

