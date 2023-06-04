#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int s_population;
    do
    {
        s_population = get_int("Starting population: ");
    }
    while (s_population < 9);
    // TODO: Prompt for end size
    int e_population;
    do
    {
        e_population = get_int("Ending population: ");
    }
    while (e_population <= s_population);
    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    do
    {
        s_population = s_population + (s_population/3) - (s_population/4);
        years++;
    }
    while (s_population < e_population);


    // TODO: Print number of years
    printf("Years: %i\n", years);
}
