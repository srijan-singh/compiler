#include<stdio.h>
#include<string.h>

char* l;

void E();

void E_();

int main()
{
	// E is a start symbol.
	E();
	
	// if lookahead = $, it represents the end of the string
	// Here l is lookahead.
	if (l == '$')
		printf("Parsing Successful");
}

// Definition of E, as per the given production
void E()
{
	if (l == 'i') {
		match('i');
		E_();
	}
}

// Definition of E' as per the given production
void E_()
{
	if (l == '+') {
		match('+');
		match('i');
		E_();

	}//The second condition of E'
	else if ( l == 'e' )
	{
	match('e');
	}
		return;
}

// Match function
match(char t)
{
	if (l == t) {
		l = getchar();
	}
	else
		printf("Error");
}
