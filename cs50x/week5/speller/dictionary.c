// Implements a dictionary's functionality

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
unsigned int w_counter = 0;

// Hash table
node *table[LENGTH][N][N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    coordinate coordinates = hash(word);

    if(table[coordinates.x][coordinates.y][coordinates.z] == NULL)
    {
        return false;
    }
    else
    {
        node *cursor = table[coordinates.x][coordinates.y][coordinates.z];

        while(cursor != NULL)
        {
            if(strcasecmp(cursor->word, word) == 0)
            {
                return true;
            }
            else
            {
                cursor = cursor->next;
            }
        }
    }
    return false;
}

// Hashes word to a number
coordinate hash(const char *word)
{
    // TODO: Improve this hash function
    coordinate algo;

    algo.x = strlen(word);
    algo.y = tolower(word[0]) - 97;
    algo.z = tolower(word[algo.x - 1]) - 97;

    return algo;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    for(int x = 0; x < LENGTH; x++)
    {
        for(int y = 0; y < N; y++)
        {
            for(int z = 0; z < N; z++)
            {
                table[x][y][z] = NULL;
            }
        }
    }

    FILE *file = fopen(dictionary, "r");

    if (!file)
    {
        printf("Error opening file!\n");
        return false;
    }

    char dword[LENGTH + 1];

    while(fscanf(file, "%s", dword) != EOF)
    {
        node *new = malloc(sizeof(node));

        if(new != NULL)
        {
            strcpy(new->word, dword);
        }

        coordinate coordinates = hash(dword);

        if(table[coordinates.x][coordinates.y][coordinates.z] == NULL)
        {
            new->next = NULL;
        }
        else
        {
            new->next = table[coordinates.x][coordinates.y][coordinates.z];
        }

        table[coordinates.x][coordinates.y][coordinates.z] = new;
        w_counter += 1;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return w_counter;
}

// Unloads dictionary from memory, returning true if successful, else false

void freenode(node *n)
{
    if(n->next != NULL)
    {
        freenode(n->next);
    }
    free(n);
}

bool unload(void)
{
    // TODO
    for(int x = 0; x < LENGTH; x++)
    {
        for(int y = 0; y < N; y++)
        {
            for(int z = 0; z < N; z++)
            {
                node *cursor = table[x][y][z];
                while(cursor != NULL)
                {
                    node *temp = cursor;
                    cursor = cursor->next;
                    freenode(temp);
                }
            }
        }
    }
    return true;
}

