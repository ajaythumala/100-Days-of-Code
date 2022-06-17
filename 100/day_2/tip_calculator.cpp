// #the tip calculator project

#include<iostream>
using namespace std;
int main()
{
    // #variable declaration
    float bill,final_amount, tip_p;
    int n_split;
    // #user greeting
    cout<<"Welcome to the tip calculator program."<<endl;
    cout<<"I shall help you calculate the total amount and the split - inclusive of the tip %"<<endl<<endl;

    // #user input
    cout<<"What was the total bill? $ ";
    cin>>bill;
    cout<<"How much tip would you like to give? 10, 12, or 15? ";
    cin>>tip_p;
    cout<<"How many people to split the bill? (Enter '1' if there's no split): ";
    cin>>n_split;

    // #calculation
    final_amount=bill*(1+(tip_p/100.0))/n_split;

    // #user output
    cout<<endl<<"Here's amount you owe - "<<final_amount;

    return 0;
}