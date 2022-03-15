#include<iostream>

using namespace std;

int count = 0;
string input;

bool match(char t);
void E();
void E_();

int main()
{
    cout<<"Please Input String: ";
    cin>>input;

    input+='$';

    E();

    if(input[count] == '$')
    {
        cout<<"Parsing Successful!";
    }

    return 0;
}

void E()
{
    if(input[count] == 'i')
    {
        if (match('i'))
        {
            E_();
        }
    }

    else
    {
        cout<<"Print Error";
    }
}

void E_()
{
    if (input[count] == '+') 
    {
        if (match('+') or match('i'))
        {
            E_();
        }
	}
    //The second condition of E'
	else if ( input[count] == 'e' )
	{
	    match('e');
	}

    else
    {
        cout<<"Print Error";
    }
}

bool match(char t)
{
    if(t == input[count])
    {
        count++;
        return true;
    }

    cout<<"\nPrint Error!";

    return false;
}