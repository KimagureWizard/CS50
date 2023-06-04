// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    int s_counter = 0;
    int n_counter = 0;
    int u_counter = 0;
    int l_counter = 0;

    for(int i=0; i < strlen(password); i++)
    {
        int c = password[i];

        if((c >= 34 && c <= 47) || (c >= 58 && c <= 64) || (c >= 91 && c <= 96) || (c>= 123 && c <= 126))
        {
            s_counter++;
        }
        if(c >= 48 && c <= 57)
        {
            n_counter++;
        }
        if(c >= 65 && c <= 90)
        {
            u_counter++;
        }
        if(c >= 97 && c <= 122)
        {
            l_counter++;
        }
    }
    
    if(s_counter > 0 && n_counter > 0 && u_counter > 0 && l_counter > 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
