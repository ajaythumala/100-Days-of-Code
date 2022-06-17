#include<iostream>
using namespace std;
int main()
{


cout<<R"(*******************************************************************************
88                                                                       88  
88                                              ,d                       88  
88                                              88                       88  
88,dPPYba,  ,adPPYYba, 88       88 8b,dPPYba, MM88MMM ,adPPYba,  ,adPPYb,88  
88P'    "8a ""     `Y8 88       88 88P'   `"8a  88   a8P_____88 a8"    `Y88  
88       88 ,adPPPPP88 88       88 88       88  88   8PP""""""" 8b       88  
88       88 88,    ,88 "8a,   ,a88 88       88  88,  "8b,   ,aa "8a,   ,d88  
88       88 `"8bbdP"Y8  `"YbbdP'Y8 88       88  "Y888 `"Ybbd8"'  `"8bbdP"Y8  
                                                                             
*******************************************************************************
)"<<"\n";



while(1>0)
{   
    //variable declaration
    char again;


    cout<<"Do you want to play again? 'y or 'n' ";
    cin>>again;
    if(again=='y')
        continue;
    else if(again=='n')
        break;
    break;
}
return 0;
}