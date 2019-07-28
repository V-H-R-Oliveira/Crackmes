#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <sys/ptrace.h>

unsigned int youwillneveeeeerwindude(int a)
{	
	if(ptrace(PTRACE_TRACEME, 0, 1, 0 == -1) && a != -1)
		return 6969;
	return 5;
}

char* function()
{
    if(ptrace(PTRACE_TRACEME, 0, 1, 0 == -1))
        return "142x142x121x1424421";
    
    return "142x142x121x1424421x";
}

void debugMe()
{
    char a[30] = "zaa4h9z1ga8ga5g1h8z4";
    char b[30] = "e18ah41z8h1ah05za9hg";
    char c[30] = "z2zh8a4g94ah1z9hg1aa";
    char d[30] = "GHh4a9hHRZJQk8z1h12z";
    
    char* s = function();
    char input[strlen(s) + 1];
    fgets(input, sizeof(input), stdin);
    char password[strlen(s) + 1];
    password[sizeof(password) - 1] = '\0';
    
    for(int i = 0; i < strlen(s); ++i)
    {
    	
        int id = s[i] - '0';
        char secretChar = '\0';
        switch(id)
        {
            case 1:
                secretChar = b[i];
                break;
            case 2:
                secretChar = a[i];
                break;
            case 3:
                secretChar = c[i];
                break;
            case 4:
                secretChar = d[i];
                break;
            default:
                secretChar = 'S';
                break;
        }
        
        int parameterValue = 0;
        if(s[strlen(s) - 1] != 'x')
        	parameterValue = -1;
        else if(s[strlen(s) - 1] == '1')
        	parameterValue = -1;
        
        unsigned int hello = youwillneveeeeerwindude(parameterValue);
        if(hello == 5 || hello == 0)
        	input[i] = '?';
        password[i] = secretChar;
    }

    if(strcmp(password, input) == 0)
        printf("YEAAAAAAAAAH YOU ARE GOOD MAN!\n");
    else
        printf("Bad password, you can buy the product by sending $10: "
        "1Fn3N79g2soMWQES2ZWVUu59Y4xKf3hWKh\n");
}
int main()
{
    debugMe();
}
