#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int check_l(string text);
int check_w(string text);
int check_s(string text);

int main(void)
{
    string text = get_string("Text: ");

    float l_count = check_l(text);

    float w_count = check_w(text);

    float s_count = check_s(text);

    float L = (l_count / w_count) * 100;

    float S = (s_count / w_count) * 100;

    float result = (0.0588 * L) - (0.296 * S) - 15.8;

    int grade = result;

    int letters = l_count;

    int words = w_count;

    int sentences = s_count;

    printf("Text: %s\n", text);

    printf("Letters count: %i\n", letters);

    printf("Words count: %i\n", words);

    printf("Sentences count: %i\n", sentences);

    if(grade < 1)
    {
        printf("Before Grade 1");
    }
    else if(grade > 16)
    {
        printf("Grade 16+");
    }
    else
    {
        printf("Grade: %i\n", grade);
    }

}


int check_l(string text)
{
    int sum = 0;

    for(int i = 0; i < strlen(text); i++)
    {
        char c = text[i];

        if(isalpha(c))
        {
            sum ++;
        }
    }
    return sum;
}

int check_w(string text)
{
    int sum = 1;

    for(int i = 0; i < strlen(text); i++)
    {
        char c = text[i];

        if(isspace(c))
        {
            sum ++;
        }
    }
    return sum;
}


int check_s(string text)
{
    int sum = 0;

    for(int i = 0; i < strlen(text); i++)
    {
        char c = text[i];
        int j = c;

        if(j == 33 || j == 46 || j == 63)
        {
            sum ++;
        }
    }
    return sum;
}
