#include <bits/stdc++.h>
#include <iostream>
#include <time.h>

using namespace std;

void append(char x,char arr[],int &z)
{
    arr[z]=x;
    z++;
}

int array_len(char array[])
{
    int i=0,count=0;
    while(i==0)
    {
        if(array[i]!='\0')
        {
            count++;
            i++;
        }
        else
            break;
    }
    return count;
}

int main()
{
    //variable declaration and assignment
    char letters[]= {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    char numbers[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    char symbols[] = {'!', '#', '$', '%', '&', '(', ')', '*', '+'};
    int nr_letters, nr_symbols, nr_numbers;
    int l_size=sizeof(letters);
    int n_size=sizeof(numbers);
    int s_size=sizeof(symbols);

    //user greeting and input 
    printf("Welcome to the PyPassword Generator!\n\n");
    printf("How many letters would you like in your password? ") ;
    cin>>nr_letters;
    printf("How many symbols would you like? ");
    cin>>nr_symbols;
    printf("How many numbers would you like? ");
    cin>>nr_numbers;
    
    //password array size determined by input size
    char password[nr_letters+nr_numbers+nr_symbols];
    int password_array_size=sizeof(password);
    int password_length;
    password_length=array_len(password);

    int i=0;
    for(i=0;i<nr_numbers;i++)
        cout<<numbers[rand() % sizeof(numbers)];
    for(i=0;i<nr_letters;i++)
        cout<<letters[rand() % sizeof(letters)];
    for(i=0;i<nr_symbols;i++)
        cout<<symbols[rand() % sizeof(symbols)];
    

}