#include <stdio.h>
#include <string.h>
#define SIZE 1024

int main(int argc, char **argv)
{
    unsigned long flag = 0;
    char username[SIZE];
    size_t username_length;
    
    if(argc == 2)
    {
        username_length = strlen(argv[1]);

        if(username_length > 1024)
        {
            fprintf(stderr, "Invalid length.\n");
            return 1;
        }

        strncpy(username, argv[1], username_length);
        username[username_length] = '\0';
        
        for(unsigned int i = 0; i < username_length; i++) 
            flag = (int)(char)username[i] + flag + (int)(char)username[i + 1];
        
        printf("Password: %ld\n", flag);
    }else
    {
        fprintf(stderr, "usage, only one arg, with valid ascii characters: ./keygen <username>\n");
        return 1;
    }

    return 0;
}
