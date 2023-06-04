#include <cs50.h>
#include <stdio.h>

int calculator(long c_num);

int main(void)
{
   long c_num;
   do
   {
        c_num = get_long ("Card number: ");
   }
   while (c_num < 0);

   calculator(c_num);
}



int calculator(long c_num)
{
   int sum = 0;
   long i_num = c_num;

   for(int i = 16; i > 0; i--)
   {
      int num_2 = ((i_num % 100) / 10) * 2;

      sum += i_num % 10;

      sum += (num_2 % 10) + ((num_2 % 100) / 10);

      i_num /= 100;
   }

   if ((c_num / 10000000000000) >= 34 && (c_num / 10000000000000) < 38 && sum % 10 == 0 )
   {
      printf("AE\n");
   }

   else if ((c_num / 100000000000) >= 40 && (c_num / 100000000000) < 50 && sum % 10 == 0)
   {
      printf("Visa\n");
   }

   else if ((c_num / 10000000000000) >= 40 && (c_num / 100000000000000) < 50 && sum % 10 == 0)
   {
      printf("Visa\n");
   }

   else if ((c_num / 100000000000000) >= 51 && (c_num / 100000000000000) < 55 && sum % 10 == 0)
   {
      printf("MC\n");
   }
   else
   {
      printf("Invalid\n");
   }
   return 0;
}

