// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(arr, n));
}

// TODO: return the max value
int max(int array[], int n)
{
    int i = 0;
    int counter = 0;

    do
    {
    if(array[i] > array[i+1])
    {
        int c = array[i];
        array[i] = array[i+1];
        array[i+1] = c;
        i++;
    }
    else if(array[i] <= array[i+1])
    {
        i++;
        counter++;
    }

    if(i == n-1 && counter != n-1)
    {
        i = 0;
        counter = 0;
    }
    else if(i == n-1 && counter == n-1)
    {
        i++;
    }
    }
    while(i < n);

    return array[n-1];
}
