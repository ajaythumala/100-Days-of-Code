#include<iostream>
using namespace std;
int main()
{
    // #the band-name generator project.

    // #variable declaration
    string name,feeling,band_name;

    // #user greeting
    cout<<"Welcome to the band name generator!"<<endl;
    cout<<"Please answer the prompts below to receive an amazing band name!"<<endl;
    cout<<"Yes, an amazing band name :)"<<endl;

    // #user input
    cout<<"---Please enter - the name of your uncle or aunty: ";
    cin>>name;
    cout<<"---Please enter - a feeling that drives your music: ";
    cin>>feeling;

    // #band name output
    band_name=name+" is feeling "+feeling;

    // #output for the user
    cout<<"The name of your band could be,\n   "+band_name;

    return 0;
}