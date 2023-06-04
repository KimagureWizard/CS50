// Practice working with structs
// Practice applying sorting algorithms

#include <cs50.h>
#include <stdio.h>

#define NUM_CITIES 10

typedef struct
{
    string city;
    int temp;
}
avg_temp;

avg_temp temps[NUM_CITIES];

void sort_cities(void);

int main(void)
{
    temps[0].city = "Austin";
    temps[0].temp = 97;

    temps[1].city = "Boston";
    temps[1].temp = 82;

    temps[2].city = "Chicago";
    temps[2].temp = 85;

    temps[3].city = "Denver";
    temps[3].temp = 90;

    temps[4].city = "Las Vegas";
    temps[4].temp = 105;

    temps[5].city = "Los Angeles";
    temps[5].temp = 82;

    temps[6].city = "Miami";
    temps[6].temp = 97;

    temps[7].city = "New York";
    temps[7].temp = 85;

    temps[8].city = "Phoenix";
    temps[8].temp = 107;

    temps[9].city = "San Francisco";
    temps[9].temp = 66;

    sort_cities();

    printf("\nAverage July Temperatures by City\n\n");

    for (int i = 0; i < NUM_CITIES; i++)
    {
        printf("%s: %i\n", temps[i].city, temps[i].temp);
    }
}

// TODO: Sort cities by temperature in descending order
void sort_cities(void)
{
    // Add your code here
    int i = 0;
    int counter = 0;
    do
    {
    if(temps[i].temp < temps[i+1].temp)
    {
        int c = temps[i].temp;
        temps[i].temp = temps[i+1].temp;
        temps[i+1].temp = c;
        string t = temps[i].city;
        temps[i].city = temps[i+1].city;
        temps[i+1].city = t;
        i++;
    }
    else if(temps[i].temp >= temps[i+1].temp)
    {
        i++;
        counter++;
    }

    if(i == 9 && counter != 9)
    {
        i = 0;
        counter = 0;
    }
    else if(i == 9 && counter == 9)
    {
        return;
    }
    }
    while(i < 10);
}
