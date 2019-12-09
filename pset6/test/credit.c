#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long creditcard;

    do
    {
    creditcard = get_long("Type card number: ");
    //printf("Stored: %ld\n", creditcard);
    }
    while (creditcard <= 0);

    int count_digits = 0;
    long creditcard_validation = creditcard;

    while (creditcard_validation > 0)
    {
        creditcard_validation = creditcard_validation / 10;
        count_digits++;

    }
    //printf("Digits: %i\n", count_digits);

    // finds the digits
    int digit1 = ((creditcard % 100 / 10) * 2);
    int digit2 = ((creditcard % 10000 / 1000) * 2);
    int digit3 = ((creditcard % 1000000 / 100000) * 2);
    int digit4 = ((creditcard % 100000000 / 10000000) * 2);
    int digit5 = ((creditcard % 10000000000 / 1000000000) * 2);
    int digit6 = ((creditcard % 1000000000000 / 100000000000) * 2);
    int digit7 = ((creditcard % 100000000000000 / 10000000000000) * 2);
    int digit8 = ((creditcard % 10000000000000000 / 1000000000000000) * 2);

    int sum1 = ((digit1 % 10) + (digit1 / 10));
    sum1 = (sum1 + ((digit2 % 10) + (digit2 / 10)));
    sum1 = (sum1 + ((digit3 % 10) + (digit3 / 10)));
    sum1 = (sum1 + ((digit4 % 10) + (digit4 / 10)));
    sum1 = (sum1 + ((digit5 % 10) + (digit5 / 10)));
    sum1 = (sum1 + ((digit6 % 10) + (digit6 / 10)));
    sum1 = (sum1 + ((digit7 % 10) + (digit7 / 10)));
    sum1 = (sum1 + ((digit8 % 10) + (digit8 / 10)));

    int digit9 = (creditcard % 10);
    int digit10 = (creditcard % 1000 / 100);
    int digit11 = (creditcard % 100000 / 10000);
    int digit12 = (creditcard % 10000000 / 1000000);
    int digit13 = (creditcard % 1000000000 / 100000000);
    int digit14 = (creditcard % 100000000000 / 10000000000);
    int digit15 = (creditcard % 10000000000000 / 1000000000000);
    int digit16 = (creditcard % 1000000000000000 / 100000000000000);

    sum1 = (sum1 + digit9 + digit10 + digit11 + digit12 + digit13 + digit14 + digit15 + digit16);


    if (count_digits == 13 && ((sum1 % 10) == 0)) //validates creditcard base on number and luhn's
    {
        printf("VISA\n");
    }

    else if (count_digits == 15)
     {
         long amex_number = (creditcard / 10000000000000);
         if ((amex_number != 34) && (amex_number != 37))
         {
             printf("INVALID3\n");
         }
         else
         {
             printf("AMEX\n");
         }
     }


    {


    }
    else if (count_digits == 16 && digit8 == 8 && ((sum1 % 10) == 0))
    {
        printf("VISA\n");
    }
    else if (count_digits == 16 && (sum1 % 10 == 0))
    {
        printf("MASTERCARD\n");

    }
    else
    {
        printf("INVALID\n");
    }

    printf("sum1: %i\n", sum1);
}
